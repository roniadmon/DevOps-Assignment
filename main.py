from datetime import datetime
from flask import Flask, request
from Logger import Logger
from Restaurant import Restaurant

app = Flask(__name__)

@app.route('/api/restaurants', methods=['POST'])
def get_restaurants():
    logger = Logger()
    time_stamp = datetime.now()
    params = request.get_json(force=True)
    logger.trace(time_stamp,"request",params)
    
    #validate_params()
    
    filtered_restaurants=Restaurant().get_restaurant_by_params(params)
    logger.trace(time_stamp,"response",filtered_restaurants)

    return filtered_restaurants

#remove before sending the solution - only for self-usage, not recuired
@app.route('/api/restaurants/add', methods=['POST'])
def add_restaurant():
    logger = Logger()
    time_stamp = datetime.now()
    logger.trace(time_stamp,"request",request.args)
    #validate
    restaurant = Restaurant()
    id = restaurant.create(request.get_json(force=True))
    logger.trace(time_stamp,"response",id)

    return id

if __name__ == '__main__':
    app.run(debug=True)