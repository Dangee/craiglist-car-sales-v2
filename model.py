"""
Model library
Setup prediction model params and initialization
"""

import params as p
import numpy as np

# create a dictionary of model intercept and coefficient values
def initialize_prediction_model(intercept, predictor_vars, predictor_coeff):
    predictor_model = {'intercept': intercept}
    for v in range(0,len(predictor_vars)):
        predictor_model[predictor_vars[v]] = predictor_coeff[v]
    return predictor_model

# reset user input
def reset_model_input(predictor_vars):
    model_input = {'intercept': 1}
    for v in range(0,len(predictor_vars)):
        model_input[predictor_vars[v]] = 0
    return model_input

# generate prediction based on user input
def generate_prediction(predictor_model, predictor_vars, model_input):
    # convert model_input
    input_array = []
    for v in predictor_vars:
        if v != 'intercept':
            input_array.append(model_input[v])

    input_array = np.array(input_array).reshape(1, -1)
    std_input_array = p.std_scaler.transform(input_array)

    prediction_value = p.lin_reg.predict(std_input_array)
    prediction = round(prediction_value[0],2)

    return prediction


# build the regression equation description
PREDICTOR_MODEL = initialize_prediction_model(p.INTERCEPT,
                                               p.PREDICTOR_VARS,
                                               p.PREDICTOR_COEFF)

