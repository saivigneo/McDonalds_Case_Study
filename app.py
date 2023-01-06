from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    yummy = float(request.form['yummy'])
    convenient = float(request.form['convenient'])
    spicy = float(request.form['spicy'])
    fattening = float(request.form['fattening'])
    greasy = float(request.form['greasy'])
    fast = float(request.form['fast'])
    cheap = float(request.form['cheap'])
    tasty = float(request.form['tasty'])
    expensive = float(request.form['expensive'])
    healthy = float(request.form['healthy'])
    disgusting = float(request.form['disgusting'])
    Like = float(request.form['Like'])
    Age = float(request.form['Age'])
    VisitFrequency = float(request.form['VisitFrequency'])
    Gender = float(request.form['Gender'])




    result = model.predict([[yummy,convenient,spicy,fattening,greasy,fast,cheap,tasty,expensive,healthy	,
    disgusting	,Like,Age,VisitFrequency,Gender]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)

