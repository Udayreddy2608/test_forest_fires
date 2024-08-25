from flask import Flask,request,jsonify,render_template,redirect,url_for
import pickle
import numpy as np
import pandas as pd

application = Flask(__name__)
app = application

ridge = pickle.load(open('/Users/sai./Documents/Projects/project1/webapp/ridge.pkl','rb'))


@app.route('/',methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/predictdata',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        temperature = float(request.form.get('Temperature'))
        rh = float(request.form.get('RH'))
        ws = float(request.form.get('Ws'))
        rain = float(request.form.get('Rain'))
        ffmc = float(request.form.get('FFMC'))
        dmc = float(request.form.get('DMC'))
        isi = float(request.form.get('ISI'))
        classes = float(request.form.get('Classes')) 
        region = float(request.form.get('region'))    # Assuming region is a string
        
        result = ridge.predict([[temperature,rh,ws,rain,ffmc,dmc,isi,classes,region]])

        return render_template('predict.html',results = round(result[0]))

    else:
        return render_template('predict.html')


if __name__=='__main__':
    app.run(debug=True)
    
