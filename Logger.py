
import json

class Logger(object):
    def __init__(self):
        config = json.load(open('config.json'))['logs']
        destination = config.get('destination')

        self.trace_func = self.get_trace_function(destination)

    def get_trace_function(self, destination):
        trace_functions = {
            'file': self.trace_to_file,
            'db': self.trace_to_db,
        }

        return trace_functions.get(destination, self.trace_to_file)

    def trace(self, time_stamp,type,data):
        self.trace_func(time_stamp,type,data)

    def trace_to_file(self,time_stamp,type,data):
        with open("trace.json",'a+') as trace_file:
            json.dump(f"{{'timeStamp':'{time_stamp}','type':'{type}','data':'{data}}}", trace_file)

    def trace_to_db(self,time_stamp,type,data):
        #file for now
        with open("trace.json",'a+') as trace_file:
            json.dump(f"{{'timeStamp':'{time_stamp}','type':'{type}','data':'{data}'}}", trace_file)