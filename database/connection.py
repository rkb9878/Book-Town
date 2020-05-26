from pymysql import *
class connections:
    def ConnectMe(self):
        con = connect("localhost", "root", "", "goodreads")
        return con