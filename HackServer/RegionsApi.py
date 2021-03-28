from flask import request, make_response
from flask_restful import abort, Resource
import json
import os
import requests

from DbHelper import *

class RegionsList(Resource):
    def __init__(self):
        self.db = DbHelper()

    def get(self):
        result_check = True
        try:
            regions = self.db.GetRegions()
            results_dict = []
            for region in regions:
                result = {
                    "id": region.GetId(),
                    "title": region.GetTitle(),
                    "description": region.GetDescription(),
                    "image_url": region.GetImageUrl(),
                    "avg_price": region.GetAvgPrice()
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
            title = data_json['title']
            description = data_json['description']
            image_url = data_json['image_url']
            avg_price = data_json['avg_price']

            max_id = self.db.GetMaxOfRegionsIds()

            img_data = requests.get(image_url).content
            filename = os.getcwd() + "/resources/regions/" + str(max_id + 1) + ".jpg"
            with open(filename, "wb") as writer:
                writer.write(img_data)

            operation_response = self.db.InsertRegionRecord(title, description, avg_price)
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

class RegionData(Resource):
    def __init__(self):
        self.db = DbHelper()

    def get(self, region_id):
        result_check = True
        try:
            record_query_result = self.db.GetRegionRecord(region_id)
            result = [{
                "id": record_query_result.GetId(),
                "title": record_query_result.GetTitle(),
                "description": record_query_result.GetDescription(),
                "image_url": record_query_result.GetImageUrl(),
                "avg_price": record_query_result.GetAvgPrice()
            }]
        except:
            result_check = False

        if not result_check:
            return [{"result": False, "data": ""}]
        else:
            result_response = [{"result": result_check, "data": result}]
            return make_response(json.dumps(result_response, ensure_ascii=False).encode('utf-8').decode('utf-8'))

    def put(self, region_id):
        data_json = request.get_json()

        result = True
        try:
            title = data_json['title']
            description = data_json['description']
            image_url = data_json['image_url']
            avg_price = data_json['avg_price']

            max_id = self.db.GetMaxOfRegionsIds()

            img_data = requests.get(image_url).content
            filename = os.getcwd() + "/resources/regions/" + str(max_id + 1) + ".jpg"
            with open(filename, "wb") as writer:
                writer.write(img_data)

            operation_response = self.db.UpdateRegionRecord(region_id, title, description, image_url, avg_price)
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