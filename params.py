"""
Params library
Define custom parameters for main app
"""

# Application log level
LOG_LEVEL = 'DEBUG'
LOG_LEVEL = 'INFO'

# Application pull down selections
FUEL_TYPE = ['gas',  'diesel', 'hybrid', 'electric', 'other']
CAR_TYPE = ['sedan', 'coupe', 'convertible', 'hatchback', 'wagon', 'mini-van', 'van', 'SUV', 'pickup', 'truck',
       'offroad', 'bus', 'other_type']
CAR_CONDITION = ['new', 'like new', 'excellent', 'good', 'fair',  'salvage']
TRANSMISSION = ['automatic', 'manual', 'other']


# Car website URL:
CAR_WEBSITE = 'https://sfbay.craigslist.org/search/cta'
# search URL https://sfbay.craigslist.org/search/cta?query=mustang+gt+convertible
IMAGE_URL = 'https://www.conceptcarz.com/'

# Google sheet with test data
GOOGLE_SHEET_TEST_DATA = 'https://docs.google.com/spreadsheets/d/11VuF8B9UZ8jdRc-3hjzTgghEVlblzMDD3TeUNmioNok/edit?usp=sharing'

# Prediction model parameters
INTERCEPT = -769538.86433 # cheat - add adjustment factor to avoid negative pricing
# INTERCEPT = -804538.8643260737

PREDICTOR_VARS = ['year',
 'odometer',
 'ferrari',
 'gas',
 'diesel',
 'other_fuel',
 'sedan',
 'pickup',
 'other_type',
 'automatic',
 'other_transmission',
 'excellent',
 'good',
 'fair']

PREDICTOR_COEFF = [390.5031441248841,
 -0.017659688952919708,
 103920.36002700841,
 1745.5726762019538,
 13946.538609987403,
 5743.117645250859,
 -4301.212153910639,
 8570.283187851448,
 3708.44941088399,
 -1170.7571963590008,
 3942.8207817679704,
 -2559.9572273672566,
 -3043.6496077529555,
 -9014.598056518584]

VERBATIMS = {
  'no_market': [
    "oh dude, I am afraid there is no market for this car. Sorry!",
    "ah, if you pay someone, they may agree to take if off your hands",
    "your car maybe worth more by selling it in the parts :-)"
 ],
  'ferrari': [
     "Ferrari - the great sports car legacy!",
     "Why oh why would you want to part with this beauty!",
     "Hey dude, are you in financial trouble? Who in their right minds would want to sell this car",
     "hey, wait a minute - this should hold on to this car now? This will likely continue to increase in value!"
  ],
 'cheap': [
    "well, nobody will break the bank for this one!"
 ],
 'antique': [
   "Ok, well, this is really an antique car",
   "wow, this car is so old... does it really still drive?",
   "oh well, you should not drive the highway with this one"
 ],
 'classic': [
   "ah, this is a classic car",
   "wait, this is really a classic car. It might continue to increase in value if you hold on to it"
 ]
}



