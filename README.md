# minidb

## objective

This is a simple database that stores data in a file. It is not intended to be used in production, but rather as a learning tool.


## modules

- `__init__.py`
- `minidb.py`

## methods

`MiniDB.__init__(self, path)` - initialize the database
`MiniDB.insert(self, data)` - insert data into the database
`MiniDB.all(self)` - return all data in the database
`MiniDB.get(self, id)` - return data with the given id
`MiniDB.update(self, id, data)` - update data with the given id
`MiniDB.delete(self, id)` - delete data with the given id
`MiniDB.delete_all(self)` - delete all data in the database