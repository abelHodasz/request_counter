from flask import Flask, request, url_for, render_template, redirect
import data_handler

app = Flask(__name__)


@app.route('/')
def route():
    return render_template('index.html')


@app.route('/request-counter', methods=['GET', 'POST'])
def route_request_counter():
    if request.method == 'POST':
        data_handler.post += 1
    if request.method == 'GET':
        data_handler.get += 1
    return redirect(url_for('route'))


@app.route('/statistics')
def route_statistics():
    return render_template('statistics.html', requests = {'GET': data_handler.get, 'POST': data_handler.post})


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )