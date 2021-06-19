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
items = []

for item in result['items']:
    items.append({
        'name': item['item_basic']['name'],
        'price': item['item_basic']['price'],
        'brand': item['item_basic']['brand']
    })

with open("result.json", 'w') as jsonFile:
    jsonFile.write(json.dumps(result, indent=4))
    jsonFile.close

with open("result-filter.json", 'w') as jsonFile:
    jsonFile.write(json.dumps(items, indent=4))
    jsonFile.close