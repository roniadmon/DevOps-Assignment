from Database import Database

class Logger(object):
    def __init__(self) -> None:
        self.collections = {"trace":"traces"}
        self.db = Database()

    def trace(self, time_stamp,type,data):
            self.db.insert(
                 {
                      'timeStamp':time_stamp,
                      'type' : type,
                      'data' : data
                 },
                 self.collections["trace"])