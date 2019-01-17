import json

related_data = []
with open("RC_2018-11.json", encoding="UTF-8") as json_file: #refer to the correct dataset
	for line in json_file:
		data_point = json.loads(line)
		if data_point['subreddit_name_prefixed'] == 'r/syriancivilwar':
			related_data.append(data_point)
			print(data_point['author_flair_text'])