from flask import Flask, render_template, jsonify
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

# Lista de datas fixas (com ou sem horas e minutos)
fixed_dates = [
    "17/05/2024", "16/08/2024 14:30", "17/08/2024 19:51", 
    "28/08/2024 16:59", "14/09/2024", "20/09/2024 17:04", 
    "12/10/2024", "09/11/2024 21:15", "16/11/2024 20:00", 
    "06/12/2024 14:59", "02/01/2025 13:25", "21/01/2025 21:40",
    "21/01/2025 21:40"
]

# Configuração para pares de imagens lado a lado
side_by_side_indices = {
    11: [11, 12],
    # Adicione novos pares aqui se necessário
    # Exemplo: 13: [13, 14],
}

def calculate_time_differences():
    current_date = datetime.now()
    results = []

    for i, fixed_date in enumerate(fixed_dates):
        try:
            # Tenta parsear com o formato completo (data + horas)
            input_date = datetime.strptime(fixed_date, "%d/%m/%Y %H:%M")
        except ValueError:
            # Se falhar, assume que é somente data (hora 00:01)
            input_date = datetime.strptime(fixed_date, "%d/%m/%Y").replace(hour=1)

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

        # Verifica se o índice está configurado como parte de um par
        if i in side_by_side_indices:
            results.append({"type": "side_by_side", "indices": side_by_side_indices[i], "time": result})
        else:
            results.append({"type": "single", "index": i, "time": result})

    return results

@app.route('/')
def home():
    return render_template('home.html')  # Página inicial "Para o meu Amor"

@app.route('/surpresa')
def surpresa():
    # Carrega a página inicial da surpresa
    return render_template('surpresa.html')

@app.route('/surpresa-data')
def surpresa_data():
    # Endpoint para fornecer os dados atualizados
    results = calculate_time_differences()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
