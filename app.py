import pickle
from flask import Flask, request, jsonify, app, url_for, render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
#Load the model
scaler = pickle.load(open("scaling.pkl", "rb"))
pickle_model1 = pickle.load(open("models/LinearRegression.pkl", "rb"))
pickle_model2 = pickle.load(open("models/RidgeCV.pkl", "rb"))
pickle_model3 = pickle.load(open("models/RandomForestRegressor.pkl", "rb"))
pickle_model4 = pickle.load(open("models/GradientBoostingRegressor.pkl", "rb"))

FEATURE_NAMES=scaler.feature_names_in_

@app.route('/')
def home():
    return render_template("home.html", best_model=None, predictions_table=[])
    #return render_template('home.html')


@app.route('/predict_api', methods=['POST'])
def predict_api():
    
    # ---- Validate request ----
    if not request.is_json or "data" not in request.json:
        return jsonify({"error": "Invalid request. JSON with 'data' required."}), 400

    ## Getting Data from request Postman API call
    data = request.json['data']
    print(data)
    
    ## Converting data into numpy array in the shape of 2D array required by sklearn models 
    #input_array = np.array(list(data.values())).reshape(1, -1)
    input_array = pd.DataFrame([data], columns=FEATURE_NAMES)
    print(input_array)

    # Scaling input data
    new_data = scaler.transform(input_array)

    # Predictions from all 4 models
    pred_linear = float(pickle_model1.predict(new_data)[0])
    pred_ridge = float(pickle_model2.predict(new_data)[0])
    pred_rf = float(pickle_model3.predict(new_data)[0])
    pred_gb = float(pickle_model4.predict(new_data)[0])

    # Store predictions in a table-like structure
    predictions_table = [
        {"model": "LinearRegression", "prediction": float(pred_linear)},
        {"model": "RidgeCV", "prediction": float(pred_ridge)},
        {"model": "RandomForestRegressor", "prediction": float(pred_rf)},
        {"model": "GradientBoostingRegressor", "prediction": float(pred_gb)}
    ]

    # Ensemble (average) prediction
    ensemble_prediction = float(
        (pred_linear + pred_ridge + pred_rf + pred_gb) / 4
    )

    # Best model selection (highest prediction)
    best_model = max(predictions_table, key=lambda x: x["prediction"])

    return jsonify({
        "predictions_table": predictions_table,
        "ensemble_prediction": ensemble_prediction,
        "best_model": best_model
    })

@app.route('/predict', methods=['POST'])
def predict():
     # Read form input
    data_dict = {name: float(val) for name, val in zip(FEATURE_NAMES, request.form.values())}
    input_array = pd.DataFrame([data_dict], columns=FEATURE_NAMES)

    # # Read form input
    # data = [float(x) for x in request.form.values()]
    # input_array = np.array(data).reshape(1, -1)

    # Scale input
    final_input = scaler.transform(input_array)

    # Predict using all 4 models
    pred_linear = float(pickle_model1.predict(final_input)[0])
    pred_ridge  = float(pickle_model2.predict(final_input)[0])
    pred_rf     = float(pickle_model3.predict(final_input)[0])
    pred_gb     = float(pickle_model4.predict(final_input)[0])

    # Store predictions
    predictions_table = [
        {"model": "LinearRegression", "prediction": float(pred_linear)},
        {"model": "RidgeCV", "prediction": float(pred_ridge)},
        {"model": "RandomForestRegressor", "prediction": float(pred_rf)},
        {"model": "GradientBoostingRegressor", "prediction": float(pred_gb)}    
    ]

    # Select best model (highest prediction)
    best_model = max(predictions_table, key=lambda x: x["prediction"])
    # Pass variables to template
    return render_template(
        "home.html",
        predictions_table=predictions_table,
        best_model=best_model
    )
    # ["model"]
    # best_prediction = max(predictions_table, key=lambda x: x["prediction"])["prediction"]
    # return render_template(
    #     "home.html",
    #     prediction_text=(
    #         f"Best Model: {best_model_name} | "
    #         f"Predicted House Price: ${best_prediction:,.2f}"
    #     )
    #)

if __name__ == "__main__":
    app.run(debug=True)     
    
# @app.route('/predict_api', methods=['POST'])
# def predict_api():
#     ## Getting Data from request Postman API call
#     data = request.json['data']
#     ## Printing row data
#     print(data)
#     ## Converting data into numpy array in the shape of 2D array required by sklearn models 
#     print(np.array(list(data.values())).reshape(1, -1))
#     ## Appliying scaling during model training
#     new_data = scaler.transform(np.array(list(data.values())).reshape(1, -1))   
#     model_type = request.json.get('model_type', 'LinearRegression')
#     data_array = np.array(list(data.values())).reshape(1, -1)
    
#     if model_type == 'LinearRegression':
#         prediction = pickle_model1.predict(new_data)
#     elif model_type == 'RidgeCV':
#         prediction = pickle_model2.predict(new_data)            
#     elif model_type == 'RandomForestRegressor':
#         prediction = pickle_model3.predict(new_data)
#     elif model_type == 'GradientBoostingRegressor':
#         prediction = pickle_model4.predict(new_data)
#     else:
#         return jsonify({'error': 'Invalid model type specified.'}), 400
    
#     return jsonify({'prediction': prediction[0]})
