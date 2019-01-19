import json

text_file = open("Authors_11_18.txt", "w", encoding="utf-8")  # change filename accordingly
related_data = []
with open("RC_2018-11", encoding="UTF-8") as json_file: #refer to the correct dataset
	for line in json_file:
		data_point = json.loads(line)
		if data_point['subreddit_name_prefixed'] == 'r/syriancivilwar':
			related_data.append(data_point)
			text_file.write(json.dumps(data_point['author']))
