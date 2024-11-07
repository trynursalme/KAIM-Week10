import os
import pandas as pd
from flask import flask, jsonify, request
from flask_cors import CORS


app = flask(__name__)
CORS(app)

# Define the data path
data_dir = os.path.join(os.path.dirname(__file__), 'data')
brent_data_path = os.path.join(data_dir, 'Copy of BrentOilPrices.csv')
gdp_data_path = os.path.join(data_dir, 'GDP.csv')
unemployment_data_path = os.path.join(data_dir, 'UNRATE.csv')

# Load data files
brent_data = pd.read_csv(brent_data_path)
gdp_data = pd.read_csv(gdp_data_path)
unemployment_data = pd.read_csv(unemployment_data_path)

# Define API endpoint

if __name__ == '__main__':
    app.run(debug=True)