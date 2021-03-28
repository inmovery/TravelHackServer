from flask import Flask, jsonify, request, Response, make_response, send_file
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
import pymysql
import pandas as pd
import json
import csv
import os
import requests

from DbHelper import *
from Models import *

from RegionsApi import *
from ImagesApi import *
from PlacesApi import *

path = os.getcwd()

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def root():
    return "Welcome, TravelHack."

# GET, POST
api.add_resource(RegionsList, '/api/regions')
api.add_resource(PlacesList, '/api/places')
# api.add_resource(CategoriesList, '/api/categories')
# api.add_resource(EventsList, '/api/events')

# GET, PUT, DELETE
api.add_resource(RegionData, '/api/regions/<int:region_id>')
api.add_resource(PlaceData, '/api/places/<int:place_id>')
# api.add_resource(CategoryData, '/api/categories/<int:region_id>')
# api.add_resource(EventData, '/api/events/<int:region_id>')

# GET
api.add_resource(ImagesForRegions, '/api/regions/images/<int:image_id>')
api.add_resource(ImagesForPlaces, '/api/places/images/<int:image_id>')
# api.add_resource(ImagesForCategories, '/api/categories/images/<int:image_id>')
# api.add_resource(ImagesForEvents, '/api/events/images/<int:image_id>')

if __name__ == '__main__':
    app.run()
