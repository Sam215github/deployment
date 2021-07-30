from flask import Flask, render_template, request
import joblib
#instance of an app
app = Flask(__name__)
model = joblib.load('dib_79.pkl')

@app.route('/')
def hello():
    return 'Hello World!!!'

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/blogs', methods = ['POST'])
def blogs_page():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin =  request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age =  request.form.get('age')

    print('fetched Input')

    pred = model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age) ]])

    if pred[0] == 1:
        result = 'the person is diabatic'

    else:
        result = 'person is not diabatic'

    return render_template('blogs.html', predicted_result = f'{result}')

if __name__=='__main__':
    app.run(debug=True)