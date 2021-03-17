import flask
from flask import Flask,request, jsonify,render_template
import numpy as np
import pickle
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('Final_model.pkl','rb'))

@app.route('/',methods=['GET'])
def home():
    return(render_template('index.html'))

@app.route('/predict',methods=['POST'])
def predict():
    train=[x for x in request.form.values()]
    airline=request.form['Airline']
    dest=request.form['Destination']
    src=request.form['Source']
    info=request.form['Additional_Info']
    if airline=='Air Asia':
    	train[0]=0
    elif airline=='Air India':
    	train[0]=1
    elif airline=='GoAir':
    	train[0]=2
    elif airline=='IndiGo':
    	train[0]=3
    elif airline=='Jet Airways':
    	train[0]=4
    elif airline=='Jet Airways Business':
    	train[0]=5
    elif airline=='Multiple carriers':
    	train[0]=6
    elif airline=='Multiple carriers Premium economy':
    	train[0]=7
    elif airline=='SpiceJet':
    	train[0]=8
    elif airline=='Trujet':
    	train[0]=9
    elif airline=='Vistara':
        train[0]=10
    elif airline=='Vistara Premium economy':
        train[0]=11
    if src=='Banglore':
    	train[1]=0
    elif src=='Chennai':
    	train[1]=1
    elif src=='Delhi':
    	train[1]=2
    elif src=='Kolkata':
    	train[1]=3
    elif src=='Mumbai':
    	train[1]=4
    
    if dest=='Banglore':
    	train[2]=0
    elif dest=='Cochin':
    	train[2]=1
    elif dest=='Delhi':
    	train[2]=2
    elif dest=='Hyderabad':
    	train[2]=3
    elif dest=='Kolkata':
    	train[2]=4
    elif dest=='New Delhi':
    	train[2]=5
    if info=='1 Long layover':
    	train[4]=0
    elif info=='1 Short layover':
    	train[4]=1
    elif info=='2 Long layover':
    	train[4]=2
    elif info=='Change airports':
    	train[4]=3
    elif info=='In-flight meal not included':
    	train[4]=4
    elif info=='No Info':
    	train[4]=5
    elif info=='No check-in baggage included':
    	train[4]=6	
    elif info=='Red-eye flight':
    	train[4]=7
    for i in range(0,len(train)):
    	train[i]=np.int(train[i])
    train=pd.DataFrame([train],columns=['Airline', 'Source', 'Destination', 'Total_Stops', 'Additional_Info',
        'Journey_day', 'Journey_month', 'Dep_hour', 'Dep_minute',
        'Arrival_hour', 'Arrival_minute', 'duration_hour', 'duration_minute'])
    #return render_template('index.html',prediction_text='Train Data {}{}{}'.format(train,train.columns,train.shape))
    y_pred=model.predict(train)
    result=round(y_pred[0],2)
    return render_template('index.html',prediction_text='The Predicted Flight Fare for the given data is {}'.format(y_pred))

if __name__=='__main__':
    app.run(debug=True)
