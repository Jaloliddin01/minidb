# minidb

## objective

This is a simple database that stores data in a file. It is not intended to be used in production, but rather as a learning tool.


## modules

- `__init__.py`
- `minidb.py`

## methods

MiniDB.__init__(self, path)
MiniDB.insert(self, data)
MiniDB.all(self)
MiniDB.get(self, id)
MiniDB.update(self, id, data)
MiniDB.delete(self, id)
MiniDB.delete_all(self)