import datetime
from Logger import Logger
from Restaurant import Restaurant
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/restaurants', methods=['POST'])
def get_restaurants():
    logger = Logger()
    time_stamp = datetime.datetime.now()
    logger.trace(time_stamp,"request",request.args)
    
    #validate_params()
    params = request.get_json(force=True)
    
    filtered_restaurants=Restaurant().get_restaurant_by_params(params)
    logger.trace(time_stamp,"response",filtered_restaurants)

    return filtered_restaurants

#remove before sending the solution - only for self-usage, not recuired
@app.route('/api/restaurants/add', methods=['POST'])
def add_restaurant():
    logger = Logger()
    time_stamp = datetime.datetime.now()
    logger.trace(time_stamp,"request",request.args)
    #validate
    restaurant = Restaurant()
    id = restaurant.create(request.get_json(force=True))
    logger.trace(time_stamp,"response",id)

    return id

if __name__ == '__main__':
    app.run(debug=True)