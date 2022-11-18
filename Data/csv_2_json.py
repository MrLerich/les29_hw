import csv
import json

ADS = 'ads'
CATEGORY = 'categories'


def convert_csv2json(csv_file, json_file, model):
    with open(csv_file, encoding='utf-8') as csv_file:
        result = []
        for row in csv.DictReader(csv_file):
            to_add = {'model': model, 'pk': int(row['Id'] if 'Id' in row else row['id'])}
            if 'id' in row:
                del row['id']
            else:
                del row['Id']

            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False

            if 'price' in row:
                row['price'] = int(row['price'])

            to_add['fields'] = row
            result.append(to_add)

    with open(json_file, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(result, ensure_ascii=False))


convert_csv2json(f'{ADS}.csv', f'{ADS}.json', 'ads.ad')
convert_csv2json(f'{CATEGORY}.csv', f'{CATEGORY}.json', 'ads.category')
