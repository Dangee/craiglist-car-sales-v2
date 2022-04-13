"""
Model library
Setup prediction model params and initialization
"""

import params as p

# create a dictionary of model intercept and coefficient values
def initialize_predictor_model(intercept, predictor_vars, predictor_coeff):
    predictor_model = {'intercept': intercept}
    for v in range(0, len(predictor_vars)):
        predictor_model[predictor_vars[v]] = predictor_coeff[v]
    return predictor_model


# reset user input
def reset_model_input(predictor_vars):
    model_input = {}
    for v in range(0, len(predictor_vars)):
        model_input[predictor_vars[v]] = 0
    model_input['intercept'] = 1
    return model_input


# generate prediction based on user input
def generate_prediction(predictor_model, model_input):
    prediction = 0
    for i in predictor_model.keys():
        prediction += predictor_model[i] * model_input[i]
    return prediction


# build the regression equation description
PREDICTOR_MODEL = initialize_predictor_model(p.INTERCEPT, p.PREDICTOR_VARS, p.PREDICTOR_COEFF)

REGRESSION_EQUATION = "Recommended Sale Price = "
for v in PREDICTOR_MODEL.keys():
    if v == "intercept":
        REGRESSION_EQUATION = REGRESSION_EQUATION + str(round(PREDICTOR_MODEL[v],5)) + " + "
    else:
        REGRESSION_EQUATION = REGRESSION_EQUATION + "(" + str(round(PREDICTOR_MODEL[v],5)) + " X " + v + ") + "

REGRESSION_EQUATION = REGRESSION_EQUATION[:-3]