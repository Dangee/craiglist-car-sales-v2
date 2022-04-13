import dash
from dash import dcc,html
from dash.dependencies import Input, Output, State

import random

import params as p
import model as m
import utils as u


########### setup app attributes and parameters
APP_TITLE = "Car sale"
STYLE_SHEETS = ['./assets/my_bWLwgP.css']
IMAGE = './1980-Ferrari-308-DV-10.jpg'

DATA_URL = 'https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data'
GITHUB_LINK = 'https://github.com/Dangee/craiglist-car-sales'

fuel_type_list = p.FUEL_TYPE
car_condition_list = p.CAR_CONDITION
car_type_list = p.CAR_TYPE
transmission_list = p.TRANSMISSION

car_website = p.CAR_WEBSITE

predictor_vars = p.PREDICTOR_VARS
predictor_coeff = p.PREDICTOR_COEFF

model_input = m.reset_model_input(predictor_vars)

########### Initiate the app
external_stylesheets = ['./assets/my_cWLwgPP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = APP_TITLE

# initiate application logger
logger = u.configure_logging()

########### Set up the layout
logger.info("setting up app layout")
app.layout = html.Div(
  children = [
    html.H1("Craig's List Car Price Predictor", className='header'),
    html.P("Considering selling your car on Craig's list? Use our sale price predictor to help you get started.",
           style={'textAlign': 'center', 'fontSize': '24px'}),
    html.Br(),
    html.Div(
      [
        html.Img(src=app.get_asset_url(IMAGE), style={'width': '30%', 'height': 'auto'}, className='four columns'),
        html.Div(
          [
            html.H3('Car Features:'),
            html.Div('Year:'),
            dcc.Input(id='year-id', type='number', min=1900, max=2022, step=1,
                      required=True, autoFocus=True, size='50px'),
            html.Div('Car type:'),
            dcc.Dropdown(id='car-type-id',
                         options=[
                           {"label": i, "value": i}
                           for i in car_type_list
                         ]),
            html.Div('Manufacter and model:'),
            dcc.Input(id='model-id', type='text', required=True, size='350px'),
            html.Div('Current odometer reading:'),
            dcc.Input(id='odometer-id', type='number', min=10, max=1000000, step=1,
                      required=True, size='100px'),
            html.Div('Car condition:'),
            dcc.Dropdown(id='condition-id',
                         options=[
                           {"label": i, "value": i}
                           for i in car_condition_list
                         ]),
            html.Div('Fuel type:'),
            dcc.Dropdown(id='fuel-id',
                         options=[
                           {"label": i, "value": i}
                           for i in fuel_type_list
                         ]),
            html.Div('Transmission type:'),
            dcc.Dropdown(id='transmission-id',
                         options=[
                           {"label": i, "value": i}
                           for i in transmission_list
                         ]),
          ],
          className='three columns'
        ),
        html.Div(
          [
            html.Button(children='Submit', id='submit-val', n_clicks=0,
                            style={
                            'background-color': 'green',
                            'color': 'white',
                            'margin-left': '5px',
                            'verticalAlign': 'center',
                            'horizontalAlign': 'center'}
                            ),
            html.H3('Predicted Sale Price:'),
            html.Div(id='results-id'),
            html.P(id='message-box-id', style = {'color': 'darkred'}),
            html.A(id='car-website-id',
                   children='TRY THIS AFTER clicking Submit: Research cars and/or post your car for sale (use right-click to open in new tab)',
                   href=car_website)
          ],
          className='four columns'
        )
      ],
      className='twelve columns',
    ),
    html.Br(),
    html.Br(),
    html.Br(),

    html.Div(children = [
        html.H4('Regression Equation:'),
        html.Div(m.REGRESSION_EQUATION, style={}),
        html.Br(),
        html.P("Note: other than year and odometer, equation variables are boolean (True = 1 or False = 0), based on user selections.")
      ]
    ),
    html.Br(),
    html.A('Google Spreadsheet', href=p.GOOGLE_SHEET_TEST_DATA),
    html.Br(),
    html.A('Code on Github', href=GITHUB_LINK),
    html.Br(),
    html.A("Data Source", href=DATA_URL),
    html.Br(),
    html.A("Car Image - courtesy of conceptcarz.com", href=p.IMAGE_URL),
  ],
  className="wrapper"
)



######### Define Callback
@app.callback(
    Output(component_id='results-id', component_property='children'),
    Output(component_id='message-box-id', component_property='children'),
    Output(component_id='car-website-id', component_property='href'),
    Input(component_id='submit-val', component_property='n_clicks'),
    State(component_id='year-id', component_property='value'),
    State(component_id='odometer-id', component_property='value'),
    State(component_id='car-type-id', component_property='value'),
    State(component_id='model-id', component_property='value'),
    State(component_id='fuel-id', component_property='value'),
    State(component_id='transmission-id', component_property='value'),
    State(component_id='condition-id', component_property='value')
)
def car_price(clicks, year, odometer, car_type,
            model, fuel, transmission, condition):
    logger.info("callback function initiated")
    prediction = "Make a selection for all car features and click Submit to see your car price!!!"
    special_message = ""
    car_website = p.CAR_WEBSITE

    if clicks==0:
        logger.debug("no clicks")
        return prediction, special_message, car_website
    else:
        logger.debug("perform prediction")
        can_perform_prediction = True

        # reset model user input
        model_input = m.reset_model_input(predictor_vars)

        # set model user input based on selections
        # set year and values to user entered values
        if year:
          model_input['year'] = year
          if year < 1925:
            special_message = random.choice(p.VERBATIMS['antique'])
          elif year < 1980:
            special_message = random.choice(p.VERBATIMS['classic'])
        else:
          can_perform_prediction = False

        if odometer:
          model_input['odometer'] = odometer
        else:
          can_perform_prediction = False

        # model is relevant for the equation only if it contains the keyword ferrari
        # the info can also be used to customize the Research cars link
        # so still requesting user to provided
        if model:
          model_input['model'] = model
          if 'ferrari' in model.lower():
            model_input['ferrari'] = 1

          # generate custom search URL
          model_search_keywords = model
          for i in ["/", ".", ",", ";", ":"]:
            model_search_keywords = model_search_keywords.replace(i, "")

          model_search_keywords = model_search_keywords.replace(" ", "+")
          car_website = p.CAR_WEBSITE + "?query=" + model_search_keywords

        else:
          can_perform_prediction = False

        # set bolean variables to True (1) for user selection
        if car_type:
          model_input[car_type] = 1
        else:
          can_perform_prediction = False

        if fuel:
          model_input[fuel] = 1
        else:
          can_perform_prediction = False

        if transmission:
          model_input[transmission] = 1
        else:
          can_perform_prediction = False

        if condition:
          model_input[condition] = 1
        else:
          can_perform_prediction = False

        if can_perform_prediction:
          prediction_value = m.generate_prediction(m.PREDICTOR_MODEL, model_input)
          prediction = "${:,.2f}".format(prediction_value)
          # prediction = model_input # debug - will through error but will display dict values in error box
          if special_message ==  "":
            if prediction_value <= 10:
              special_message = random.choice(p.VERBATIMS['no_market'])
            elif prediction_value <= 1000:
              special_message = random.choice(p.VERBATIMS['cheap'])
        else:
          special_message = "Please provide an input to all the features before clicking the Submit button"

    logger.info(model_input)
    logger.info(f"App response: {prediction}")
    logger.info(f"Special message: {special_message}")

    return prediction, special_message, car_website


############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
