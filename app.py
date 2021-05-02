from flask import Flask
from flask_restful import Api, Resource, abort
from bs4 import BeautifulSoup
import csv, requests
import pandas
import lxml
 
app = Flask(__name__) 
api = Api(app)

class table_filter(Resource): 
    def get(self): 
        return {'hello': 'world'}


api.add_resource(table_filter, '/')

if __name__ == '__main__': 
    app.run(debug=True)