from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bonjour depuis mon API DevOps ! 🚀</h1><p>Inchallah ça marche !</p>"

@app.route('/health')
def health():
    return {"status": "OK", "message": "Application déployée avec succès !"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
