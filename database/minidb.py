## MINI DATABASE BY JALOLIDDIN
import json
from os.path import exists
class MiniDB():
    def __init__(self, file_name):
        if exists(f'{file_name}.json'):
            with open(f'{file_name}.json', 'r') as db:
                self.db = json.load(db)
                self.filename = f'{file_name}.json'
        else:
            with open(f'{file_name}.json', 'w') as db:
                initial = {"_database": []}
                self.db = initial
                db.write(json.dumps(self.db, indent=4))
                self.filename = f'{file_name}.json'
    
    def save(self):
        with open(self.filename, 'w') as db:
            db.write(self.db)
    
    def insert(self, data):
        with open(self.filename, 'r') as db:
            all_data = json.load(db)
            all_data['_database'].append(data)
            self.db = json.dumps(all_data, indent=4)
        self.save()

    def remove(self, data):
        with open(self.filename, 'r') as db:
            all_data = json.load(db)
            all_data['_database'].remove(data)
            self.db = json.dumps(all_data, indent=4)
        self.save()

    def remove_all(self):
        with open(self.filename, 'r') as db:
            all_data = json.load(db)
            all_data['_database'].clear()
            self.db = json.dumps(all_data, indent=4)
        self.save()

    def update(self):
        pass

    def all(self):
        with open(self.filename, 'r') as db:
            return db


# def main():
#     db = MiniDB("data")
#     db.insert({'type': 'peach', 'count': 12})
#     print(db.all())


# if __name__ == "__main__": 
#     main()


        