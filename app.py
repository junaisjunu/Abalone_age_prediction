from flask import Flask, render_template, request, send_file
import pandas as pd
from src.components.prediction import Prediction
from src import logger
from src.config.configuration import Configuration
from src.components.bulk_prediction import BulkPredction

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    form_data = {
        'Sex': request.form['sex'],
        'Length': float(request.form['length']),
        'Diameter': float(request.form['diameter']),
        'Height': float(request.form['height']),
        'Whole weight': float(request.form['whole_weight']),
        'Whole weight.1': float(request.form['whole_weight_1']),
        'Whole weight.2': float(request.form['whole_weight_2']),
        'Shell weight': float(request.form['shell_weight'])
    }
    data = pd.DataFrame([form_data])
    data['Sex'] = data['Sex'].map({'Male': 'M', 'Female': 'F', 'Infant': 'I'})
    logger.info(data)
    logger.info(data.info())

    config = Configuration()
    prediction_config = config.get_prediction_config()
    model_predictor = Prediction(prediction_config)
    prediction = round(model_predictor.initiate_prediction(data=data)[0], 2)
    return render_template('prediction.html', prediction=prediction)


@app.route('/bulk-prediction')
def bulk_prediction_form():
    return render_template('bulk_prediction_form.html')


@app.route('/bulk_predict', methods=['POST'])
def bulk_predict():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        df = pd.read_csv(file)
        bulk_pred = BulkPredction()
        output_file_path = bulk_pred.initiate_bulk_prediction(data=df)
        reult_data = pd.read_csv(output_file_path)
        top_20_data = reult_data.head(20)
    return render_template('bulk_predict.html', tables=[top_20_data.to_html(classes='data')], titles=top_20_data.columns.values, result_file=output_file_path)


@app.route('/download/<filename>')
def download(filename):
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
