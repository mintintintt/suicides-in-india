import json
import pygal
with open('data.json') as data_file:
    data = json.load(data_file)

dic = {}
for i in data:
    if i['State'] in dic:
        dic[i['Year']] += i['Total']
    else:
        dic[i['Year']] = i['Total']

chart = pygal.Bar()
for i in dic.keys():
    chart.add(str(i), dic[i])
chart.render_to_file('chart.svg')
print('OK')
print(dic)

