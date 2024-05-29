import json

datafile = open("webinars.json","rb")   #открыть файл, положили его в переменную datafile
data = json.load(datafile)  #прочитать файл в формате json, в прерменую data
datafile.close()
[print(webinar["speaker"]) for webinar in data] #списковое выражение для каждого вебинара вывести его спикера

