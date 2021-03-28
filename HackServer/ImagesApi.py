from flask import send_file
from flask_restful import abort, Resource

# def HandleImagesGetRequest(type_name, image_id):
#     try:
#         filename = '../resources/' + type_name + '/' + str(image_id) + '.jpg'
#         return send_file(filename)
#     except:
#         return abort(204)

class ImagesForRegions(Resource):
    def get(self, image_id):
        try:
            filename = '../resources/regions/' + str(image_id) + '.jpg'
            return send_file(filename)
        except:
            return abort(204)

class ImagesForEvents(Resource):
    def get(self, image_id):
        try:
            filename = '../resources/events/' + str(image_id) + '.jpg'
            return send_file(filename)
        except:
            return abort(204)

class ImagesForPlaces(Resource):
    def get(self, image_id):
        try:
            filename = '../resources/places/' + str(image_id) + '.jpg'
            return send_file(filename)
        except:
            return abort(204)
