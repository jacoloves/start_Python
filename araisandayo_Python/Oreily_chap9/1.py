import  urllib.request as ur
url = 'https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/fortune_cookie_random1.txt'
conn = ur.urlopen(url)
print(conn)

data = conn.read()
print(data)