class Logger(object):
    def trace(self,time_stamp,type,data):
        trace_file = open("trace.json",'a+')
        trace_file.writelines(f"{{'timeStamp':'{time_stamp}','type':'{type}','data':'{data}'}}")
        trace_file.close