from flask import Flask, render_template, jsonify 
from flask_restful import Api, Resource, abort
import requests
import pandas as pd
from pandas import json_normalize
 
app = Flask(__name__) 
api = Api(app)

def check_link(request): 
    if request.status > 200: 
        abort(400, message="Connection Error")
    else: 
        return True

class filter_table(Resource): 

    def get(self, search, table_num, top_n): 

        response = requests.get(f'https://wikipedia-table-scraper.herokuapp.com/search/{search}/{table_num}')
        data = response.json()

        if top_n == None: 

            json_data = pd.DataFrame(data)

        else: 
            df = pd.DataFrame(data)
            filter_df = df.head(top_n)
            json_data = filter_df.to_dict()

        return jsonify(json_data)

@app.route('/')
def description(): 
    return ("This is a simple microservice that pulls and filters Wikipedia tables.")

api.add_resource(filter_table, "/filter/<string:search>/<int:table_num>/<int:top_n>")

if __name__ == '__main__': 
    app.run(debug=True, port=5001)