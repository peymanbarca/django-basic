
class NativeQueryUtil:
    def __init__(self, cursor):
        self.cursor = cursor

    def queryBuilder(self):
        pass

    def queryExecutor(self,query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data


