import flask
from flask import render_template
from variables import *

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                       COVID_PROPORTION_SOUTHEAST = COVID_PROPORTION_SOUTHEAST,
                       COVID_PROPORTION_NORTHEAST = COVID_PROPORTION_NORTHEAST,
                       COVID_PROPORTION_MIDWEST = COVID_PROPORTION_MIDWEST,
                       COVID_PROPORTION_SOUTH = COVID_PROPORTION_SOUTH,
                       COVID_PROPORTION_NORTH = COVID_PROPORTION_NORTH,
                       BRAZIL_REGIONS = BRAZIL_REGIONS,
                       POPULATION_SOUTHEAST = SOUTHEAST_POPULATION,
                       POPULATION_NORTHEAST = NORTHEAST_POPULATION,
                       POPULATION_MIDWEST = MIDWEST_POPULATION,
                       POPULATION_SOUTH = SOUTH_POPULATION,
                       POPULATION_NORTH = NORTH_POPULATION,
                       COVID_CASES_BRAZIL = BRAZIL_CASES_COVID,
                       COVID_CASES_SOUTHEAST = SOUTHEAST_COVID_CASES,
                       COVID_CASES_NORTHEAST = NORTHEAST_COVID_CASES,
                       COVID_CASES_MIDWEST = MIDWEST_COVID_CASES,
                       COVID_CASES_SOUTH = SOUTH_COVID_CASES,
                       COVID_CASES_NORTH = NORTH_COVID_CASES,
                       COVID_DEATHS_BRAZIL = BRAZIL_DEATHS_COVID,
                       COVID_DEATHS_SOUTHEAST = SOUTHEAST_COVID_DEATHS,
                       COVID_DEATHS_NORTHEAST = NORTHEAST_COVID_DEATHS,
                       COVID_DEATHS_MIDWEST = MIDWEST_COVID_DEATHS,
                       COVID_DEATHS_SOUTH = SOUTH_COVID_DEATHS,
                       COVID_DEATHS_NORTH = NORTH_COVID_DEATHS,
                       POPULATION_BRAZIL = BRAZIL_POPULATION)

if __name__ == '__main__':
    app.run(debug=True)
