import requests
import json

endpoint = "https://www.semrush.com/analytics/ta/data"
headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhbGxvd2VkIjpbeyJsaW1pdCI6MTAwMCwibWF4X3JlcXVlc3RzIjoxMDAwLCJ0eXBlIjoicmFuayJ9XSwiY29kZSI6MjAwLCJleHBpcmVzX2F0IjoxNjA0MzM0OTk4LCJob3N0IjpbXSwiaXNfZGVtb19kb21haW4iOnRydWUsImxpbWl0IjoxMDAwMDAsInByb2R1Y3QiOiIiLCJ0YV9hbGxvd2VkIjp0cnVlLCJ0eXBlIjoidHJhZmZpY19yYW5rIn0.tNcAPHsYFzWagCPegS3TtiTcZff-FUXVneHpeXzqYZs"}
top_5000_offsets = list(map(lambda x: x*1000, range(0, 5)))
other_offsets = list(map(lambda x: x*1000, range(5, 100)))
top_5000_sites = []
other_sites = []

for offset in top_5000_offsets:
	params = {"key": "12acf06f164c8bf29f21eb1b355ec729", "type": "rank", "limit": 1000, "offset": offset}
	response = requests.get(endpoint, params=params, headers=headers).json()

	for item in response["items"]:
		top_5000_sites.append(item["domain"])

with open('top_5000_sites.json', 'w') as f:
    json.dump(top_5000_sites, f)

for offset in other_offsets:
	params = {"key": "12acf06f164c8bf29f21eb1b355ec729", "type": "rank", "limit": 1000, "offset": offset}
	response = requests.get(endpoint, params=params, headers=headers).json()

	for item in response["items"]:
		other_sites.append(item["domain"])

with open('5001_to_100000_sites.json', 'w') as f:
    json.dump(other_sites, f)