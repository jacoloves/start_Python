import datetime, json
now = datetime.datetime.utcnow()
print(now)

now_str = str(now)
print(json.dumps(now_str))

from time import mktime
now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))

class DTEncoder(json.JSONDecoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        return json.JSONEncoder.default(self, obj)

print(json.dumps(now, cls=DTEncoder))