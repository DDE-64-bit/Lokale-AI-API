# Lokale AI API
Ik heb met een python webserver een API endpoint opgezet die korte eenmalige AI promtpts kan ontvangen en het resultaat terug sturen.

## Gebruik
1. Installeer het bestand ```main.py```. 
2. Installeer [ollama](https://ollama.com/download), en een bijbehorend LLM.
3. Zet de naam van jouw LLM in de variabele ```taalModel```. 
4. Start dan het programma op.
5. Test de API door een van de onderstaande commands.

```bash
curl -X POST http://127.0.0.1:5000/send_prompt -H "Content-Type: application/json" -d "{\"prompt\": \"Hello world\"}"
```

```powershell
Invoke-WebRequest -Uri http://127.0.0.1:5000/send_prompt -Method POST -Body '{"prompt": "Hello, world"}' -ContentType "application/json"
```


## Tools en Technologieën

Dit project maakt gebruik van de volgende tools en technologieën:
- **Programmeertaal:** Python
- **Libraries:** Flask, Subprocess, Logging en Requests*
- **Vereisten:** Ollama en een LLM model**

\* Requests is alleen voor het test programma wat erbij zit.
<br>
** Het liefst een [llama](https://ollama.com/library) model.
