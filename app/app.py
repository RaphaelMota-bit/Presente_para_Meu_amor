from datetime import datetime
from dateutil.relativedelta import relativedelta
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # Página inicial "Para o meu Amor"

@app.route('/surpresa')
def surpresa():
    # Lista de datas fixas (inclui opcionalmente horas e minutos)
    fixed_dates = ["17/05/2024", "16/08/2024 14:30", "17/08/2024 19:51", "28/08/2024 16:59", "14/09/2024","20/09/2024 17:04" ,"12/10/2024", "09/11/2024 21:15", "16/11/2024 20:00" , "06/12/2024 14:59"]
    current_date = datetime.now()

    # Variável para armazenar os resultados
    results = []

    # Loop para calcular a diferença para cada data fixa
    for fixed_date in fixed_dates:
        try:
            # Tenta parsear com o formato completo (com horas e minutos)
            input_date = datetime.strptime(fixed_date, "%d/%m/%Y %H:%M")
        except ValueError:
            # Caso falhe, assume 1h da madrugada
            input_date = datetime.strptime(fixed_date, "%d/%m/%Y").replace(hour=1, minute=0)

        # Calcula a diferença de tempo
        delta = relativedelta(current_date, input_date)

        # Formata o resultado, apenas mostrando os minutos e ocultando as outras unidades se forem zero
        result = ""
        if delta.years > 0:
            result += f"{delta.years} ano{'s' if delta.years != 1 else ''}, "
        if delta.months > 0:
            result += f"{delta.months} mes{'es' if delta.months != 1 else ''}, "
        if delta.days > 0:
            result += f"{delta.days} dia{'s' if delta.days != 1 else ''}, "
        if delta.hours > 0:
            result += f"{delta.hours} hora{'s' if delta.hours != 1 else ''}, "

        # Sempre mostra os minutos, mesmo que seja zero
        result += f"{delta.minutes} minuto{'s' if delta.minutes != 1 else ''}"

        # Sempre mostra os segundos, mesmo que seja zero
        result += f" e {delta.seconds} segundo{'s' if delta.seconds != 1 else ''}"

        # Adiciona o resultado à lista de resultados
        results.append((fixed_date, result))

    # Renderiza o template HTML passando as datas e seus respectivos resultados
    return render_template('surpresa.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
