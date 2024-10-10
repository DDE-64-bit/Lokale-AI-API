import requests

# URL van je API
api_url = 'http://127.0.0.1:5000/send_prompt'

print("Welkom jouw eigen API, probeer eens wat te sturen! Typ 'exit' om de chat te beëindigen.")

while True:
    # Vraag de gebruiker om invoer
    gebruikers_prompt = input("Jij: ")

    # Controleer of de gebruiker wil afsluiten
    if gebruikers_prompt.lower() in ['exit', 'quit']:
        print("De API connectie wordt beëindigd. Tot ziens!")
        break

    # Stel de promptgegevens in
    prompt_data = {
        'prompt': gebruikers_prompt
    }

    try:
        # Stuur een POST-verzoek naar de API
        response = requests.post(api_url, json=prompt_data)

        # Controleer of het verzoek succesvol was
        if response.status_code == 200:
            # Haal de reactie van de API op
            resultaat = response.json()
            print("API: ", resultaat.get('response'))
        else:
            print(f"Fout: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print("HTTP-request mislukt:", e)
