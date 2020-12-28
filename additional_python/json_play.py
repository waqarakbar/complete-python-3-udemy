import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    the_file = open("./ages.json", "r+")
    data = json.loads(the_file.read())
    print("current age is", data['age'], "-- adding 1 year--")
    data["age"] = data["age"] + 1
    print("new age is", data["age"])
else:
    the_file = open("ages.json", "w+")
    data = {"name": "Nick Fury", "age": 25}
    print("no file found, setting default age to", data['age'])

the_file.seek(0)
the_file.write(json.dumps(data))

the_file.close()