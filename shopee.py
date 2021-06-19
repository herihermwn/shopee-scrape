import requests
import json

keyword = 'sepatu'

params = (
    ('by', 'relevancy'),
    ('keyword', keyword),
    ('limit', '100'),
    ('newest', '0'),
    ('official_mall', '1'),
    ('order', 'desc'),
    ('page_type', 'search'),
    ('scenario', 'PAGE_MALL_SEARCH'),
    ('version', '2'),
)

response = requests.get('https://shopee.co.id/api/v4/search/search_items', params=params)
result = json.loads(response.text)

for item in result['items']:
    print(item['item_basic']['name'])
    print(item['item_basic']['price'])

with open("result.json", 'w') as jsonFile:
    jsonFile.write(json.dumps(result, indent=4))
    jsonFile.close