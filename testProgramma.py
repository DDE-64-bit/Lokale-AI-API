import requests

api_url = 'http://127.0.0.1:5000/send_prompt'

print("Welkom jouw eigen API, probeer eens wat te sturen! Typ 'exit' om de chat te beëindigen.")

while True:
    gebruikers_prompt = input("Jij: ")

    if gebruikers_prompt.lower() in ['exit', 'quit']:
        print("De API connectie wordt beëindigd. Tot ziens!")
        break

    prompt_data = {
        'prompt': gebruikers_prompt
    }

    try:
        response = requests.post(api_url, json=prompt_data)

        if response.status_code == 200:
            resultaat = response.json()
            print("API: ", resultaat.get('response'))
        else:
            print(f"Fout: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print("HTTP-request mislukt:", e)
