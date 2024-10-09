from fastapi import FastAPI
import subprocess

app = FastAPI()

# Functie om een commando uit te voeren en de output te krijgen
def run_command(question: str):
    subprocess.Popen("ollama run llama2-uncensored")
    
    process = subprocess.Popen(question, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    
    # Haal de output op
    output, error = process.communicate()
    
    if error:
        return f"Error: {error}"
    
    return output.strip()

@app.get("/get-message")
async def read_root(question: str = "echo"):
    # Voer het commando uit in de achtergrond-shell
    output = run_command(f'{question}')
    
    return {"Message": f"", "Command Output": output}
