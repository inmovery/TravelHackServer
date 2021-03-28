from flask import request, make_response
from flask_restful import abort, Resource
import json
import os
import requests
from datetime import datetime, date, time

from DbHelper import *


class PlacesList(Resource):
    def __init__(self):
        self.db = DbHelper()

    def get(self):
        result_check = True
        try:
            places = self.db.GetPlaces()
            results_dict = []
            for place in places:

                category_name = self.db.GetPlaceNameByCategory(place.GetCategory())
                category_image = "https://inmovery.ru/api/categories/images/" + str(place.GetId())

                result = {
                    "id": place.GetId(),
                    "title": place.GetTitle(),
                    "details": place.GetDetails(),
                    "category_id": place.GetCategory(),
                    "category_name": category_name,
                    "category_image": category_image,
                    "latitude": place.GetLatitude(),
                    "longitude": place.GetLongitude(),
                    "image_url": place.GetImageUrl(),
                    "price": place.GetPrice()
                }
                results_dict.append(result)
            
            results = [result for result in results_dict]
        except:
            result_check = False

        if not result_check:
            return [{"result": False, "data": ""}]
        else:
            result_response = [{"result": result_check, "data": results}]
            return make_response(json.dumps(result_response, ensure_ascii=False).encode('utf-8').decode('utf-8'))

    def post(self):
        data_json = request.get_json()

        result = True
        try:
            title = data_json["title"]
            details = data_json["details"]
            category = data_json["category"]
            latitude = data_json["latitude"]
            longitude = data_json["longitude"]
            image_url = data_json["image_url"]
            price = data_json["price"]

            max_id = self.db.GetMaxOfPlacesIds()

            img_data = requests.get(image_url).content
            filename = os.getcwd() + "/resources/places/" + str(max_id + 1) + ".jpg"
            with open(filename, "wb") as writer:
                writer.write(img_data)

            operation_response = self.db.InsertPlaceRecord(title, details, category, latitude, longitude, price)
            if not operation_response:
                result = False

            self.db.DisposeConnection()
        except:
            result = False

        response = [{"result": result}]
        if result:
            return response, 201
        else:
            return response, 400

class PlaceData(Resource):
    def __init__(self):
        self.db = DbHelper()

    def get(self, place_id):
        result_check = True
        try:
            record_query_result = self.db.GetPlaceRecord(place_id)
            result = [{
                "id": record_query_result.GetId(),
                "title": record_query_result.GetTitle(),
                "details": record_query_result.GetDetails(),
                "category": record_query_result.GetCategory(),
                "latitude": record_query_result.GetLatitude(),
                "longitude": record_query_result.GetLongitude(),
                "image_url": record_query_result.GetImageUrl(),
                "price": record_query_result.GetPrice()
            }]
        except:
            result_check = False

        if not result_check:
            return [{"result": False, "data": ""}]
        else:
            result_response = [{"result": result_check, "data": result}]
            return make_response(json.dumps(result_response, ensure_ascii=False).encode('utf-8').decode('utf-8'))

    def put(self, place_id):
        data_json = request.get_json()

        result = True
        try:
            title = data_json['title']
            details = data_json['details']
            category = data_json['category']
            latitude = data_json['latitude']
            longitude = data_json['longitude']
            image_url = data_json['image_url']
            price = data_json['price']

            max_id = self.db.GetMaxOfPlacesIds()

            img_data = requests.get(image_url).content
            filename = os.getcwd() + "/resources/places/" + str(max_id + 1) + ".jpg"
            with open(filename, "wb") as writer:
                writer.write(img_data)

            operation_response = self.db.UpdatePlaceRecord(place_id, title, details, category, latitude, longitude, image_url, price)
            if not operation_response:
                result = False

            self.db.DisposeConnection()
        except:
            result = False

        response = [{"result": result}]
        if result:
            return response, 200
        else:
            return response, 400

    def delete(self, place_id):
        result = True
        try:
            result_query = self.db.DeletePlaceRecord(place_id)

            if not result_query:
                result = False

            self.db.DisposeConnection()
        except:
            result = False

        response = [{"result": result}]

        if result_query:
            return response, 200
        else:
            return abort(204)