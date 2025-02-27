import urllib.request
import json

# using urllib.request can open urlopen then read the response into json
query_url = "https://services2.arcgis.com/5I7u4SJE1vUr79JC/arcgis/rest/services/UniversityChapters_Public/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
with urllib.request.urlopen(query_url) as response:
    body_json = response.read()

# parses a valid json obj to a dict
body_dict = json.loads(body_json)

# writes the dict to a json file
output_dir = "D:\\Perforce\\playground\\unreal_python_scripting\\Plugins\\test_python_plugin\\Content\\Python\\ExternalJson\\test_api_output.json"
with open(output_dir, "w") as outfile:
    json.dump(body_dict, outfile, indent=4, ensure_ascii=False)