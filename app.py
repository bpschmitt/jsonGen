from faker import Faker
import json

fake = Faker()

def getNum(min,max):
    return fake.pyint(min_value=min,max_value=max)


print(json.dumps({"somethingElse": getNum(0,50), "orderCount" : getNum(100,400)}))
