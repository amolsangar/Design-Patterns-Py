from abc import ABC, abstractmethod

class IDatabase(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(IDatabase):
    def connect(self):
        return f"MySQL DB"

class PostgreSQL(IDatabase):
    def connect(self):
        return f"PostgreSQL DB"

class MongoDB(IDatabase):
    def connect(self):
        return f"MongoDB DB"

class Cassandra(IDatabase):
    def connect(self):
        return f"Cassandra DB"

class Redis(IDatabase):
    def connect(self):
        return f"Redis DB"
    

class DBFactory():
    dbs = {
        "mysql": MySQL,
        "postresql": PostgreSQL,
        "mongodb": MongoDB,
        "cassandra": Cassandra,
        "redis": Redis
    }

    @staticmethod
    def get_db(db_name):
        return DBFactory.dbs[db_name]()


# Client Code
db_names = ["mysql","redis"]
for name in db_names:
    db = DBFactory().get_db(name)
    print(db.connect())
    print()
