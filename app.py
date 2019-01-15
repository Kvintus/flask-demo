from flask import Flask, render_template, request, url_for
import led

cervena = led.Led(18)
modra = led.Led(17)
biela = led.Led(27)

app = Flask(__name__) 

## Here comes the magic ##

@app.route('/led', methods = ['POST'])
def led():
    re = request.get_json('led').get('led')
    if re == 'blue':
        modra.toggle()
    elif  re == 'red':
        cervena.toggle()
    elif  re == 'white':
        biela.toggle()
    
    return '', 204

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)