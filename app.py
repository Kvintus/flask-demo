from flask import Flask, render_template, request, url_for
# import led

# cervena = led.Led(23)
# modra = led.Led(18)
# biela = led.Led(24)

app = Flask(__name__) 

## Here comes the magic ##

@app.route('/led')
def led():
    return 'peter'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)