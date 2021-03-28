import config
import pymysql
from Models import *

class DbHelper():
    def __init__(self):
        self.connection = pymysql.connect(config.DB_HOST, config.DB_USERNAME, config.DB_PASSWORD, config.DB_NAME)

    def DisposeConnection(self):
        self.connection.commit()
        self.connection.close()

    def GetRegions(self):
        regions = []

        cursor = self.connection.cursor()
        query_regions = "SELECT * FROM regions"
        cursor.execute(query_regions)

        for region in cursor.fetchall():
            region_id = region[0]
            title = region[1]
            description = region[2]
            image_url = region[3]
            image_id = region[4]

            result = Region(region_id, title, description, image_url, image_id)
            regions.append(result)

        return regions

    def GetMaxOfRegionsIds(self):
        cursor = self.connection.cursor()
        query_max_id = "SELECT MAX(id) FROM regions"
        cursor.execute(query_max_id)

        result = cursor.fetchone()[0]

        if result is None:
            return 0
        else:
            return result

    def InsertRegionRecord(self, title, description, avg_price):
        cursor = self.connection.cursor()

        query_max_image_id = "SELECT MAX(id) FROM regions"
        cursor.execute(query_max_image_id)

        image_id = None
        max_image_id = cursor.fetchone()[0]
        if max_image_id is None:
            image_id = 1
        else:
            image_id = max_image_id + 1

        image_url = "https://inmovery.ru/api/regions/images/" + str(image_id)

        result_query = True
        try:
            query = f"INSERT INTO regions (title, description, image_url, avg_price) VALUES ('{title}','{description}','{image_url}', '{avg_price}')"
            cursor.execute(query)
        except:
            result_query = False

        return result_query

    def GetRegionRecord(self, region_id):
        cursor = self.connection.cursor()

        region_record_query = f"SELECT * FROM regions WHERE id = {region_id}"
        cursor.execute(region_record_query)

        region = cursor.fetchone()

        title = region[1]
        description = region[2]
        image_url = region[3]
        avg_price = region[4]

        result = Region(region_id, title, description, image_url, avg_price)
        return result

    def UpdateRegionRecord(self, region_id, title, description, image_url, avg_price):
        cursor = self.connection.cursor()

        result_query = True
        try:
            update_query = f"UPDATE regions SET title = '{title}', description = '{description}', image_url = '{image_url}'," \
                           f"avg_price = {avg_price} WHERE id = {region_id}"
            cursor.execute(update_query)
        except:
            result_query = False

        return result_query

    def DeleteRegionRecord(self, region_id):
        cursor = self.connection.cursor()

        result_query = True
        try:
            query_delete_region = f"DELETE FROM regions WHERE id = {region_id}"
            cursor.execute(query_delete_region)
        except:
            result_query = False

        return result_query

    #
    # ================================================================
    #

    def GetPlaces(self):
        places = []

        cursor = self.connection.cursor()
        query_places = "SELECT * FROM places"
        cursor.execute(query_places)

        for place in cursor.fetchall():
            place_id = place[0]
            title = place[1]
            details = place[2]
            category = place[3]
            latitude = place[4]
            longitude = place[5]
            image_url = place[6]
            price = place[7]

            result = Place(place_id, title, details, category, latitude, longitude, image_url, price)
            places.append(result)

        return places

    def GetMaxOfPlacesIds(self):
        cursor = self.connection.cursor()
        query_max_id = "SELECT MAX(id) FROM places"
        cursor.execute(query_max_id)

        result = cursor.fetchone()[0]

        if result is None:
            return 0
        else:
            return result

    def InsertPlaceRecord(self, title, details, category, latitude, longitude, price):
        cursor = self.connection.cursor()

        query_max_image_id = "SELECT MAX(id) FROM places"
        cursor.execute(query_max_image_id)

        image_id = None
        max_image_id = cursor.fetchone()[0]
        if max_image_id is None:
            image_id = 1
        else:
            image_id = max_image_id + 1

        image_url = "https://inmovery.ru/api/places/images/" + str(image_id)

        result_query = True
        try:
            query = f"INSERT INTO places (title, details, category, latitude, longitude, image_url, price)" \
                    f"VALUES ('{title}', '{details}', {category}, {latitude}, {longitude}, '{image_url}', {price})"
            cursor.execute(query)
        except:
            result_query = False

        return result_query

    def GetPlaceRecord(self, place_id):
        cursor = self.connection.cursor()

        place_record_query = f"SELECT * FROM places WHERE id = {place_id}"
        cursor.execute(place_record_query)

        place = cursor.fetchone()

        title = place[1]
        details = place[2]
        category = place[3]
        latitude = place[4]
        longitude = place[5]
        image_url = place[6]
        price = place[7]

        result = Place(place_id, title, details, category, latitude, longitude, image_url, price)
        return result

    def GetPlaceNameByCategory(self, category_id):
        cursor = self.connection.cursor()

        category_record_query = f"SELECT title FROM categories WHERE id = {category_id}"
        cursor.execute(category_record_query)

        category = cursor.fetchone()[0]

        return category

    def UpdatePlaceRecord(self, place_id, title, details, category, latitude, longitude, image_url, price):
        cursor = self.connection.cursor()

        result_query = True
        try:
            update_query = f"UPDATE places SET title = '{title}', details = '{details}', category = {category}," \
                           f"latitude = {latitude}, longitude = {longitude}, image_url = '{image_url}', price = {price} WHERE id = {place_id}"
            cursor.execute(update_query)
        except:
            result_query = False

        return result_query

    def DeletePlaceRecord(self, place_id):
        cursor = self.connection.cursor()

        result_query = True
        try:
            query_delete_region = f"DELETE FROM places WHERE id = {place_id}"
            cursor.execute(query_delete_region)
        except:
            result_query = False

        return result_query

    #
    # ================================================================
    #

    def GetEvents(self):
        events = []

        cursor = self.connection.cursor()
        query_events = "SELECT * FROM events"
        cursor.execute(query_events)

        for event in cursor.fetchall():
            place_id = event[0]
            title = event[1]
            details = event[2]
            category = event[3]
            organization = event[4]
            start_at = event[5]
            close_at = event[6]
            latitude = event[7]
            longitude = event[8]
            price = event[9]

            result = Event(place_id, title, details, category, work_at, work_end, latitude, longitude, image_id, image_url, price)
            events.append(result)

        return places

    def GetMaxOfPlacesIds(self):
        cursor = self.connection.cursor()
        query_max_id = "SELECT MAX(id) FROM places"
        cursor.execute(query_max_id)

        result = cursor.fetchone()[0]

        if result is None:
            return 0
        else:
            return result

    def InsertPlaceRecord(self, title, details, category, latitude, longitude, image_url, price):
        cursor = self.connection.cursor()

        query_max_image_id = "SELECT MAX(image_id) FROM places"
        cursor.execute(query_max_image_id)

        image_id = None
        max_image_id = cursor.fetchone()[0]
        if max_image_id is None:
            image_id = 1
        else:
            image_id = max_image_id + 1

        result_query = True
        try:
            query = f"INSERT INTO places (title, details, category, latitude, longitude, image_id, image_url, avg_price)" \
                    f"VALUES ('{title}', '{details}', {category}, {latitude}, {longitude}, {image_id}, '{image_url}', {price})"
            cursor.execute(query)
        except:
            result_query = False

        return result_query
