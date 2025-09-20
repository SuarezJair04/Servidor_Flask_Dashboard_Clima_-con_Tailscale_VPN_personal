# ╔═══════════════════════════════════════════════════════════════╗
# ║        🌤️ Mini Dashboard del Clima con Flask + Tailscale       ║
# ║        Lenguajes de Interfaz - TECNM / ITT - 2025              ║
# ║        Autor: Suarez Castro Jair Alberto                       ║
# ║        Descripción: Servidor Flask consultando OpenWeatherMap  ║
# ╚═══════════════════════════════════════════════════════════════╝

from flask import Flask
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "5b47b6c7ed03bca400cfeb4808a334a0"
CITY = "Tijuana"

@app.route("/")
def clima():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=es"
    data = requests.get(url).json()

    temp = round(data["main"]["temp"])
    weather = data["weather"][0]["description"].capitalize()
    date = datetime.now().strftime("%A, %d %B %Y")

    # Plantilla HTML con estilos parecidos al ejemplo
    return f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #cfe8ff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background: linear-gradient(90deg, #4facfe, #00f2fe);
                border-radius: 20px;
                padding: 20px 40px;
                display: flex;
                align-items: center;
                color: white;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                max-width: 500px;
            }}
            .info {{
                flex: 1;
            }}
            .temp {{
                font-size: 48px;
                font-weight: bold;
                margin: 0;
            }}
            .weather {{
                font-size: 20px;
                margin-bottom: 10px;
            }}
            .date {{
                font-size: 16px;
            }}
            .location {{
                margin-top: 5px;
                font-size: 16px;
            }}
            .sun {{
                width: 80px;
                height: 80px;
                border-radius: 50%;
                background: radial-gradient(circle, #FFD93D, #FF8400);
                box-shadow: 0 0 40px rgba(255, 200, 0, 0.8);
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="info">
                <div class="weather">{weather}</div>
                <div class="temp">{temp}°</div>
                <div class="date">{date}</div>
                <div class="location">📍 {CITY}</div>
            </div>
            <div class="sun"></div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
