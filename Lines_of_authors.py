import json
import sys

def lines_of_authors(infile, outfile):
    
    text_file = open(outfile, "w", encoding="utf-8") 
    related_data = []
    with open(inflike, encoding="UTF-8") as json_file:
        for line in json_file:
            data_point = json.loads(line)
            if data_point['subreddit_name_prefixed'] == 'r/syriancivilwar':
                related_data.append(data_point)
                text_file.write(json.dumps(data_point['author']))

if __name__ == "__main__":
    if len(sys.argv) in [1,2]:
        print("Usage: " + sys.argv[0] + "<infile> <outfile>")
    else:
        lines_of_authors(sys.argv[1], sys.argv[2])
        