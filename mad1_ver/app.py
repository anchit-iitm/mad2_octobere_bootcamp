from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/helloworld')
def hello_world():
    return 'Hello, World! from anchit'

@app.route('/test')
def test():
    return render_template('index.html')


@app.route('/test12345')
def test1():
    msg = 'hi campers'
    var2 = True
    var4 = ['iitm', 'iitkgp', 'iitb', 'iitd']
    return render_template('index1.html', var1=msg, var3=var2, var5=var4)

@app.route('/test2', methods=['GET', 'POST'])
def test2():
    if request.method == "POST":
        name_var = request.form.get('name')
        print(name_var)
        return render_template('index2.html')
    # if request.method == "GET":
    #     return render_template('index2.html')
    return render_template('index2.html')

@app.route('/test3', methods=['POST'])
def test3():
    name_var = request.form.get('name')
    print(name_var)
    # return redirect('/test1')
    return redirect(url_for('test1'))

@app.route('/test4/<int:var1>', methods=['PUT'])
def test4(var1):
    name_var = request.form.get('name')
    print(name_var, var1)
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)