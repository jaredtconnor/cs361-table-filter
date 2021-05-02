from flask import Flask, request, jsonify 
import requests
import json
import pandas as pd
from pandas import json_normalize
 
app = Flask(__name__) 
# api = Api(app)

@app.route('/')
def root(): 
    sample_text = 'Simple microservice to pull data via https://cs361-table-scraper.herokuapp.com/ service'

    wiki_page = request.args.get('wiki_page')
    table_num = request.args.get('table_num')
    num_rows = int(request.args.get('num_rows'))

    response = requests.get(f'https://cs361-table-scraper.herokuapp.com/{wiki_page}/{table_num}')
    data = response.json()

    df = pd.DataFrame.from_dict(data)
    filter_df = df.head(num_rows)
    json_data = filter_df.to_dict()

    return jsonify(json_data)
    
if __name__ == '__main__': 
    app.run(debug=True)