import json
def WriteJson(json_file):
    with open("sample.json", "w") as out_json:
        out_json.write(str(json_file))