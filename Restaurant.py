import json
from Database import Database

class Restaurant(object):
    def __init__(self) -> None:
        self.db = Database()
        self.collection_name = 'restaurants'

        #for the validator
        self.fields = { 
            "name": "string",
            "style": "string",
            "address": "string",
            "openHour": "string",
            "closeHour": "string",
            "vegetarian" : "bool"
        }

    def create(self, restaurant):
        # Validator will throw error if invalid
        #self.validator.validate(resaturant, self.fields, self.create_required_fields, self.create_optional_fields)
        return self.db.insert(restaurant, self.collection_name)

    def find(self, restaurant):
        return self.db.find(restaurant, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, restaurant):
        #self.validator.validate(restaurant, self.fields, self.update_required_fields, self.update_optional_fields)
        return self.db.update(id, restaurant,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)
    
    def get_all_from_file(self):
        with open("resturants.json") as restaurants_file : return json.load(restaurants_file)
    
    def get_restaurant_by_params(self, params):
        #validate
        if 'hour' in params:
            params['openHour'] = {'$lte' : params['hour']}
            params['closeHour'] = {'$gte' : params['hour']}
            del params['hour']
        recommended = list(self.db.find(criteria=params,collection_name=self.collection_name ))

        return recommended