from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import InputData, PreditctPipeline

# Flask(__name__) gives us the entry point
application = Flask(__name__)
app = application

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['GET','POST'])
def predict_data():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = InputData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            math_score=float(request.form.get('math_score'))
        )

        data_df = data.get_data_as_dataFrame()
        print(data_df)

        predict_pipeline = PreditctPipeline()
        predictions = predict_pipeline.predict(data_df)
        return render_template('home.html', results=predictions[0])

if __name__=="__main__":
    app.run(host="localhost")