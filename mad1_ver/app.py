from flask import Flask, render_template

app = Flask(__name__)

@app.route('/helloworld')
def hello_world():
    return 'Hello, World! from anchit'

@app.route('/test')
def test():
    return render_template('index.html')


@app.route('/test1')
def test1():
    msg = 'hi campers'
    var2 = True
    var4 = ['iitm', 'iitkgp', 'iitb', 'iitd']
    return render_template('index1.html', var1=msg, var3=var2, var5=var4)

if __name__ == '__main__':
    app.run(debug=True)