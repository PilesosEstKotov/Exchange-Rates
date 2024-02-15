import requests
import json
from flask import Flask

app = Flask(__name__)

def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes

def create_html(valutes):
    text = '<h1>Курс валют</h1>'
    text += '<table border="1">'  # Добавил рамку для таблицы
    text += '<tr>'
    # Указываем названия столбцов (заголовки)
    if valutes:
        for key in valutes[0].keys():
            text += f'<th>{key}</th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr>'
        for value in valute.values():
            text += f'<td>{value}</td>'
        text += '</tr>'
    text += '</table>'
    return text

@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)  # Явно указываем, что хотим запустить сервер на порту 5000