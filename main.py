import requests
import json

key = '0c2b659d2fca47cda3933237172607'
city = 'London'
url = 'http://api.apixu.com/v1/current.json?key=0c2b659d2fca47cda3933237172607&q=' + city
r = requests.get(url)
a = json.loads(r.content)
print r.content

temp_c = a['current']['temp_c']
temp_f = a['current']['temp_f']

f = open('./index.html', 'r+')
lines = f.readlines()
f.seek(0)
f.truncate()
for line in lines:
  if len(line) > 29:
    target = line[4:29]
  else:
    target = ""
  if target == '<div class="temperature">':
    line = '    <div class="temperature">' + str(temp_f) + ' &#8457</div>' + '\n'
  f.write(line + '')
f.close()
