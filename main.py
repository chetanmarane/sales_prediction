
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("input.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        #  reading the inputs given by the user
        tv=float(request.form['TV'])
        radio = float(request.form['Radio'])
        newspaper = float(request.form['Newspaper'])


        filename = 'finalized_model.pickle'
        loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
        # predictions using the loaded model file
        prediction=loaded_model.predict([[tv,radio,newspaper]])
        print('prediction is', prediction)
        # showing the prediction results in a UI
        return render_template('input.html',prediction=round(100*prediction[0]))

    else:
        return render_template('input.html')



if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True) # running the app