import pymysql


class sql_conn(object):
    def __init__(self, host='localhost', port=3306, user='root', password='mysql', database, charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database, charset='utf8')
        self.cursor = self.conn.cursor()


    def exit_sql(self):
        try:
            self.cursor.close()
        except Exception as e:
            pass
        try:
            self.conn.close()
        except Exception as e:
            pass
        print('SQL connect had closed.')


    def close_corsor(self):
        try:
            self.cursor.close()
        except Exception as e:
            pass
    
    def create_cursor(self):
        try:
            self.conn.cursor()
        except Exception as e:
            pass


