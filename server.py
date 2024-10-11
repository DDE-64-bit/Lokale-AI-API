from flask import Flask, request, jsonify
import subprocess
import logging

taalModel = "hierNaamTaalModel"

app = Flask(__name__)

@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Geen prompt opgegeven"}), 400

    logging.debug(f"Versturen prompt naar model: {prompt}")

    try:
        # Start het model subprocess en haal het resultaat op
        resultaat = subprocess.run(
            ['ollama', 'run', taalModel],
            input=prompt, 
            text=True,
            capture_output=True,
            check=True,
            encoding='utf-8'  # Voeg dit toe om Unicodeproblemen te voorkomen
        )
        logging.debug(f"Model output: {resultaat.stdout.strip()}")
        return jsonify({"response": resultaat.stdout.strip()})

    except subprocess.CalledProcessError as e:
        logging.error(f"Fout bij het uitvoeren van het model: {e.stderr.strip()}")
        return jsonify({"error": "Het uitvoeren van het model is mislukt"}), 500
    except Exception as e:
        logging.error(f"Onverwachte fout: {e}")
        return jsonify({"error": "Er is een onverwachte fout opgetreden."}), 500

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='127.0.0.1', port=5000)
