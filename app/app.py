from flask import Flask, render_template, jsonify
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
import os

app = Flask(__name__)

caminho = r"C:\Users\rapha\Desktop\Presente_para_Meu_amor\app"
# nome_do_arquivo = "eventos.json"
caminho_para_Arquivo = os.path.join(caminho, "eventos.json")

with open(caminho_para_Arquivo, 'r' , encoding= 'utf-8') as file:
    events = json.load(file)

def calculate_time_difference(event_date):
    current_date = datetime.now()
    try:
        input_date = datetime.strptime(event_date, "%d/%m/%Y %H:%M")
    except ValueError:
        input_date = datetime.strptime(event_date, "%d/%m/%Y").replace(hour=1)

    delta = relativedelta(current_date, input_date)
    result = ""

    if delta.years > 0:
        result += f"{delta.years} ano{'s' if delta.years > 1 else ''}, "
    if delta.months > 0:
        result += f"{delta.months} mes{'es' if delta.months > 1 else ''}, "
    if delta.days > 0:
        result += f"{delta.days} dia{'s' if delta.days > 1 else ''}, "
    if delta.hours > 0:
        result += f"{delta.hours} hora{'s' if delta.hours > 1 else ''}, "

    result += f"{delta.minutes} minuto{'s' if delta.minutes != 1 else ''}"
    result += f" e {delta.seconds} segundo{'s' if delta.seconds != 1 else ''}"
    return result

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/surpresa')
def surpresa():
    return render_template('surpresa.html')

@app.route('/surpresa-data')
def surpresa_data():
    results = []
    for event in events:
        time_diff = calculate_time_difference(event['date'])
        results.append({
            "title": event['title'],       # nome correto
            "images": event['images'],     # 👈 aqui estava o problema!
            "time": time_diff              # nome correto
        })
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
