"""
Params library
Define custom parameters for main app
"""

import pickle
import sklearn

# Application log level
LOG_LEVEL = 'DEBUG'
LOG_LEVEL = 'INFO'

# read in predictor model objects
with open('./analysis/components_data/predictor_model.pkl', 'rb') as f:
  predictor_model = pickle.load(f)

with open('./analysis/components_data/std_scaler.pkl', 'rb') as f:
  std_scaler = pickle.load(f)

with open('./analysis/components_data/lin_reg.pkl', 'rb') as f:
  lin_reg = pickle.load(f)

with open('./analysis/components_data/predictor_model.pkl', 'rb') as f:
  predictor_model = pickle.load(f)

with open('./analysis/components_data/app_categories.pkl', 'rb') as f:
  app_categories = pickle.load(f)


# Prediction model parameters
INTERCEPT = predictor_model['lin_reg']['intercept']
PREDICTOR_VARS = predictor_model['predictor_vars']
PREDICTOR_COEFF = predictor_model['lin_reg']['coeff']


# Application pull down selections
FUEL_TYPE = app_categories['fuel_type']
TRANSMISSION = app_categories['transmission']
DRIVE = app_categories['drive']
CAR_TYPE = app_categories['car_type']
CAR_CONDITION = app_categories['car_condition']
ODOMETER_CAT = app_categories['odometer_cat']

# Car website URL:
CAR_WEBSITE = 'https://sfbay.craigslist.org/search/cta'
IMAGE_URL = 'https://www.conceptcarz.com/'


VERBATIMS = {
  'no_market': [
    "oh dude, I am afraid there is no market for this car. Sorry!",
    "ah, if you pay someone, they may agree to take if off your hands",
    "your car maybe worth more by selling it in the parts :-)",
    "sorry to be bearer of bad news, but your car is not worth much :-(",
    "oh boy, maybe you should donate this car instead of selling it"
 ],
  'ferrari': [
     "Ferrari - the great sports car legacy!",
     "Why oh why would you want to part with this beauty!",
     "Hey dude, are you in financial trouble? Who in their right minds would want to sell this car",
     "hey, wait a minute - this should hold on to this car now? This will likely continue to increase in value!"
  ],
 'cheap': [
    "well, nobody will break the bank for this one!",
    "ah, look at that, what a deal!",
    "is that what we call a clunker?"
 ],
 'antique': [
   "Ok, well, this is really an antique car",
   "wow, this car is so old... does it really still drive?",
   "oh well, you should not drive the highway with this one"
 ],
 'classic': [
   "ah, this is a classic car",
   "wait, this is really a classic car. It might continue to increase in value if you hold on to it",
 ]
}



