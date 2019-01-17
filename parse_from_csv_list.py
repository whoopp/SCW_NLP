import json
import csv

with open('To_parse_flair_list.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    flairlist = [row['Flair'] for row in reader]


def downloadtext(flair: object) -> object:
    text_file = open(flair + "11_18.txt", "w", encoding="utf-8")  # change filename accordingly
    related_data = []
    with open("RC_2018-11.json", encoding="UTF-8") as json_file:  # refer to the correct dataset
        for line in json_file:
            data_point = json.loads(line)
            if data_point['subreddit_name_prefixed'] == 'r/syriancivilwar':  # limit to the right sub
                if data_point['author_flair_text'] == flair:  # limit to the correct flair
                    related_data.append(data_point)
                    text_file.write(json.dumps(data_point['body']))  # refer to the correct data point


for span in flairlist:
    flair = span
    downloadtext(flair)