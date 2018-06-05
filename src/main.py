from pymongo import MongoClient
from bson.objectid import ObjectId

# connect to database
client = MongoClient('mongodb://localhost:27017')

# get the collection
grades = client.tracker.grades

#find all restaurants in Manhattan
# for r in restaurants.find({'borough':'Manhattan'})


# d = {}
# for _ in range(3):
#     name =  input('student name:')
#     klass = input('student class:')
#     grade = float(input('grade:'))
#     # d['name'] = name
#     d = {'name': name, 'klass': klass, 'grade':grade}
#     # print(name, klass, grade)
#     grades.insert_one(d)

total = 0
count = grades.find().count()
for g in grades.find():
    print('g is', g['grade'])
    total += g['grade']
print(total)
print(total/count)

