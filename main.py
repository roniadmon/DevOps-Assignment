import Logger
import datetime
import DataReader 
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    logger = Logger.Logger()
    time_stamp = datetime.datetime.now()
    logger.trace(time_stamp,"request",request.args)
    
    #validate_params()
    params = request.args.to_dict()
    
    data_reader = DataReader.DataReader()
    filtered_restaurants=data_reader.get_by_params(params)
    logger.trace(time_stamp,"response",filtered_restaurants)

    return filtered_restaurants

if __name__ == '__main__':
    app.run(debug=True)