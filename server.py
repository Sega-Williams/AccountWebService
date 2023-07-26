from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('interaction.html')

@app.route('/interaction', methods=['GET', 'POST'])
def interaction():
    if request.method == 'POST':
        # Обработка данных, полученных от пользователя
        data = request.form.get('data')
        # Выполнение необходимых действий с данными
        result = process_data(data)
        return render_template('interaction.html', result=result)
    else:
        return render_template('interaction.html')

def process_data(data):
    # Выполнение необходимых действий с данными
    # Например, обработка данных и возврат результата
    return data.upper()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
