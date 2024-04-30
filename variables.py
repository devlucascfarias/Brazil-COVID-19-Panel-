import pandas as pd

def format_number(number):
    formatted = "{:,.0f}".format(number).replace(",", "x").replace(".", ",").replace("x", ".")
    return formatted

dataset = pd.read_excel('data.xlsx')
columns = ['População', 'Casos Acumulados', 'Óbitos Acumulados']

for col in columns:
    if dataset[col].dtype == 'object':
        dataset[col] = dataset[col].str.replace(',', '').astype(float)

BRAZIL_REGIONS = dataset['Região']

BRAZIL_POPULATION = format_number(dataset['População'].sum())
BRAZIL_CASES_COVID = format_number(dataset['Casos Acumulados'].sum())
BRAZIL_DEATHS_COVID = format_number(dataset['Óbitos Acumulados'].sum())

SOUTHEAST_POPULATION = format_number(dataset['População'][0])
NORTHEAST_POPULATION = format_number(dataset['População'][1])
MIDWEST_POPULATION = format_number(dataset['População'][2])
SOUTH_POPULATION = format_number(dataset['População'][3])
NORTH_POPULATION = format_number(dataset['População'][4])

SOUTHEAST_COVID_CASES = format_number(dataset['Casos Acumulados'][0])
NORTHEAST_COVID_CASES = format_number(dataset['Casos Acumulados'][1])
MIDWEST_COVID_CASES = format_number(dataset['Casos Acumulados'][2])
SOUTH_COVID_CASES = format_number(dataset['Casos Acumulados'][3])
NORTH_COVID_CASES = format_number(dataset['Casos Acumulados'][4])

SOUTHEAST_COVID_DEATHS = format_number(dataset['Óbitos Acumulados'][0])
NORTHEAST_COVID_DEATHS = format_number(dataset['Óbitos Acumulados'][1])
MIDWEST_COVID_DEATHS = format_number(dataset['Óbitos Acumulados'][2])
SOUTH_COVID_DEATHS = format_number(dataset['Óbitos Acumulados'][3])
NORTH_COVID_DEATHS = format_number(dataset['Óbitos Acumulados'][4])

COVID_PROPORTION_SOUTHEAST = round(dataset['População'][0] / dataset['Casos Acumulados'][0], 2)
COVID_PROPORTION_NORTHEAST = round(dataset['População'][1] / dataset['Casos Acumulados'][1], 2)
COVID_PROPORTION_MIDWEST = round(dataset['População'][2] / dataset['Casos Acumulados'][2], 2)
COVID_PROPORTION_SOUTH = round(dataset['População'][3] / dataset['Casos Acumulados'][3], 2)
COVID_PROPORTION_NORTH = round(dataset['População'][4] / dataset['Casos Acumulados'][4], 2)
