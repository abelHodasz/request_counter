from flask import Flask, request, url_for, render_template,redirect


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def route():
    return render_template('ndex.html')


@app.route('/request-counter')
def route_request_counter():
    pass


@app.route('/statistics')
def route_statistics():
    pass


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )