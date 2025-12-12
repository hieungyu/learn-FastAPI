thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 0
}
print(thisdict["brand"]) # tức là cái dict này sẽ lấy ra key của value đó
print(thisdict)
print(len(thisdict))
# print(thisdict["Mustang"]) # nếu là value thì  sẽ không chính xác

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))
# => có thể tạo nhiều dict cùng tên nhưng nếu trong key-value có cùng  giá trị thì nó sẽ lấy giá trị sau cùng
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2021
}
print(thisdict)
print(len(thisdict))
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)