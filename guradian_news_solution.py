import json


guardian_file = open('guardian-3-jan.json', encoding='utf_8')
guardian_json = json.load(guardian_file)
article_list = guardian_json['response']['results']
for index, article in enumerate(article_list):
    print(f'{index} {article["webTitle"]}')
