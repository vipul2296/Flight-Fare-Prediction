import flask
from flask import Flask,request, jsonify,render_template
import numpy as np
import pickle

app=Flask(__name__)
model=pickle.load(open('D:\iSmile Technologies\Side Projects\Flight Fare prediction\Final_model.pkl','rb'))

@app.route('/',methods=['GET'])
def home():
    render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    y=[int(x) for x in request.form.values]
    print(y)
    #y_pred=model.predict([np.array(y)])
    #result=round(y_pred[0],2)
    return render_template('index.html',prediction_text='The Predicted Flight Fare for the given data is ${}')

if __name__=='__main__':
    app.run(debug=True)