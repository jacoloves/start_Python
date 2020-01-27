import redis
conn = redis.Redis()

conn.set('select', 'ni!')

