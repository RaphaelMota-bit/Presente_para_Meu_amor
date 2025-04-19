from flask import Flask, render_template, jsonify
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

# Lista de eventos com título, data e imagens
events = [
    {
        "title": "O tempo da minha felicidade:",
        "date": "17/05/2024",
        "images": ["fotoInicial.jpg"]
    },
    {
        "title": "Nosso Praiou:",
        "date": "16/08/2024 14:30",
        "images": ["maonorosto.jpg"]
    },
    {
        "title": "Aniversário da Lavínia:",
        "date": "17/08/2024 19:51",
        "images": ["niverL.jpg"]
    },
    {
        "title": "Juntinhos na cama:",
        "date": "28/08/2024 16:59",
        "images": ["fotonacama.jpg"]
    } ,
    {
        "title": "Sapecagem: ",
        "date": "14/09/2024",
        "images": ["fotobanheiro.jpg"]
    } ,
    {
        "title": "Praiouu: ",
        "date": "20/09/2024 17:04",
        "images": ["praia2.jpg"]
    },
    {
        "title": "Festa a fantasia: ",
        "date": "12/10/2024",
        "images": ["festafantasia.jpg"]
    },
    {
        "title": "SD house: ",
        "date": "09/11/2024 21:15",
        "images": ["fotoespelho.jpg"]
    },
    {
        "title": "Aniversário da sua tia: ",
        "date": "16/11/2024 20:00",
        "images": ["aniversário da sua tia.jpg"]
    },
    {
        "title": "Nosso piscinou: ",
        "date": "06/12/2024 14:59",
        "images": ["piscina.jpg"]
    },
    #12
    {
        "title": "Nossa primeira viagem: ",
        "date": "02/01/2025 13:25",
        "images": ["nossa_primeira_viagem.jpg"]
    },
    {
        "title": "Sonho realizado",
        "date": "21/01/2025 21:40",
        "images": ["flores1.jpg", "flores2.jpg"]
    },
    {
        "title": "Realizando metas: ",
        "date": "05/02/2025 10:00",
        "images": ["linguinha.jpg","cabelo_liso.jpg","vinhada.jpg"]
    },
    {
        "title": "Meu melhor aniversário:",
        "date": "08/03/2025 12:00",
        "images": ["meu_aniversário_1.jpg", "meu_aniversário_2.jpg", "meu_aniversário_3.jpg"]
    }
    # Adicione mais eventos aqui conforme necessário
]

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
