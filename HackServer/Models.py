class Region():
	def __init__(self, region_id, title, description, image_url, avg_price):
		self.id = region_id
		self.title = title
		self.description = description
		self.image_url = image_url
		self.avg_price = avg_price

	def GetId(self):
		return self.id

	def GetTitle(self):
		return self.title

	def GetDescription(self):
		return self.description

	def GetImageUrl(self):
		return self.image_url

	def GetAvgPrice(self):
		return self.avg_price

class Place():
	def __init__(self, place_id, title, details, category, latitude, longitude, image_url, price):
		self.place_id = place_id
		self.title = title
		self.details = details
		self.category = category
		self.latitude = latitude
		self.longitude = longitude
		self.image_url = image_url
		self.price = price

	def GetId(self):
		return self.place_id

	def GetTitle(self):
		return self.title

	def GetDetails(self):
		return self.details

	def GetCategory(self):
		return self.category

	def GetLatitude(self):
		return self.latitude

	def GetLongitude(self):
		return self.longitude

	def GetImageUrl(self):
		return self.image_url

	def GetPrice(self):
		return self.price

class Category():
	def __init__(self, category_id, title, details, image_url):
		self.id = category_id
		self.title = title
		self.details = details
		self.image_url = image_url

	def GetId(self):
		return self.category_id

	def GetTitle(self):
		return self.title

	def GetDetails(self):
		return self.details

	def GetImageUrl(self):
		return self.image_url

class Event():
	def __init__(self, event_id, title, details, category, organization, latitude, longitude, start_at, close_at, image_url, price):
		self.event_id = event_id
		self.title = title
		self.details = details
		self.category = category
		self.organization = organization
		self.latitude = latitude
		self.longitude = longitude
		self.start_at = start_at
		self.close_at = close_at
		self.image_url = image_url
		self.price = price

	def GetId(self):
		return self.event_id

	def GetTitle(self):
		return self.title

	def GetDetails(self):
		return self.details

	def GetCategory(self):
		return self.category

	def GetOrganization(self):
		return self.organization

	def GetLatitude(self):
		return self.latitude

	def GetLongitude(self):
		return self.longitude

	def GetStartAt(self):
		return self.start_at

	def GetCloseAt(self):
		return self.close_at

	def GetImageUrl(self):
		return self.image_url

	def GetPrice(self):
		return self.price
