# Lokale AI API
Ik heb met een python webserver een API endpoint opgezet die korte eenmalige AI promtpts kan ontvangen en het resultaat terug sturen.

## Tools en Technologieën

Dit project maakt gebruik van de volgende tools en technologieën:
- **Programmeertaal:** Python
- **Libraries:** Flask, Subprocess, Logging en Requests*
- **Vereisten:** Ollama en een LLM model**

\* Requests is alleen voor het test programma wat erbij zit.
<br>
** Het liefst een [llama](https://www.llama.com/) model.

Invoke-WebRequest -Uri http://127.0.0.1:5000/send_prompt -Method POST -Body '{"prompt": "Hello, world"}' -ContentType "application/json"
