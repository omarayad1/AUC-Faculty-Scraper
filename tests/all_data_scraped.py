from departments import departments
import json
import HTMLParser
data = open('../output.json')
data = json.load(data)

for department in departments:
	department = HTMLParser.HTMLParser().unescape(department)
	for person in data:
		if unicode(department) == person['department_value']:
			break
	else:
		print department