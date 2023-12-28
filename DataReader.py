import json

class DataReader(object):
    def get_all(self):
        resturants_file = open("resturants.json")
        resturants = json.load(resturants_file)
        resturants_file.close
        return resturants
    
    def get_by_params(self, params):
        all_resturants = self.get_all()
        recommended = [restaurant for restaurant in all_resturants if all(restaurant[key] == value for key, value in params.items())]
        return recommended