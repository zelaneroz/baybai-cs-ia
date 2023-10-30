import sqlite3

class database_handler:
    def __init__(self,namedb:str):
        self.connection = sqlite3.Connection(namedb)
        self.cursor = self.connection.cursor()

    def run_query(self, query: str):
        self.cursor.execute(query)
        self.connection.commit()
    def close(self):
        self.connection.close()
    def search(self,query:str):
        result = self.cursor.execute(query).fetchall()
        return [item[0] for item in result]

    def search2(self,query:str):
        result = self.cursor.execute(query).fetchall()
        return result