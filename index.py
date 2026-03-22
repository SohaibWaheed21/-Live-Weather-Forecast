from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route("/")
def main():
    try:
        return render_template("index.html")
    except Exception as e:
        print("🔥 ERROR:", e)
        return str(e)

@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    try:
        raw_data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+userText+"&appid=bbc89cdfd9370ef7032feefc6a46e4f2")
        result = raw_data.json()
        return result
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
