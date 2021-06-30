import json


# from tinydb import TinyDB, Query
# db = TinyDB('chess_db.json')
# Fruit = Query()
# # db.insert({'type': 'apple', 'count': 7})
# # db.insert({'type': 'peach', 'count': 3})
# x = db.search(Fruit.type == 'apple')

# # print(x)
# # print(type(x))

f = 'chess_db.json'

print(json.dumps(f, indent=2))
  