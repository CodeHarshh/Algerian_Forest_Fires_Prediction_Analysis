from flask import Flask,request,render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application



#import Ridge pickel model

ridge_model=pickle.load(open('models/ridge.pkl','rb'))
Standard_Scaler=pickle.load(open('models/scaler.pkl','rb'))



@app.route('/')
def index():
    return render_template('main.html')

@app.route('/predictiondata',methods=['GET','POST'])
def prediction_data():
   if request.method=='POST':
   
        temperature = float(request.form['temperature'])
        rh = float(request.form['rh'])
        ws =float( request.form['ws'])
        rain = float(request.form['rain'])
        ffmc = float(request.form['ffmc'])
        dmc = float(request.form['dmc'])
        isi = float(request.form['isi'])
        classes = float(request.form['Classes'])
        region = float(request.form['Region'])

        new_data_scaled=Standard_Scaler.transform([[temperature,rh,ws,rain,ffmc,dmc,isi,classes,region]])
        results=ridge_model.predict(new_data_scaled)
        print(results)
 
        return render_template('home.html',results=results[0]) 
   else:
       return render_template('home.html')
          
# @app.route('/home',methods=['GET'])
# def home_page():

 
if __name__ == '__main__':
    app.run(debug=True)
