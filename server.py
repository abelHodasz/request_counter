from flask import Flask, request, url_for, render_template, redirect
import data_handler

app = Flask(__name__)


@app.route('/')
def route():
    return render_template('index.html')


@app.route('/request-counter', methods=['GET', 'POST', 'DELETE', 'PUT'])
def route_request_counter():
    data_handler.increment_request(request.method)
    return redirect(url_for('route'))


@app.route('/statistics')
def route_statistics():
    return render_template('statistics.html', requests = data_handler.read_requests_from_file())


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )