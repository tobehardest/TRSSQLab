import os
import json
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application =get_wsgi_application()
from django.db import transaction

from api.models import ChengduData  # 替换为您的实际模型
from api.models import *

def process_line(line,ChengduData,ChengduQuery):
    parts = line.strip().split(',')
    query_instance, _ = ChengduQuery.objects.get_or_create(id=(int(parts[0])+1))
    data_instance, _ = ChengduData.objects.get_or_create(id=(int(parts[1])+1))
    return {
        'queryid': query_instance,
        'dataid': data_instance,
        'start': int(parts[2]),
        'end': int(parts[3]),
        'score': float(parts[4])
    }

def import_data(filepath, model,ChengduData,ChengduQuery, batch_size=15000):
    with open(filepath, 'r') as file:
        batch = []
        for line in file:
            data = process_line(line,ChengduData,ChengduQuery)
            batch.append(model(**data))

            if len(batch) >= batch_size:
                with transaction.atomic():
                    model.objects.bulk_create(batch)
                batch = []

        if batch:  # 插入剩余的数据
            with transaction.atomic():
                model.objects.bulk_create(batch)

def batch_import(directory_path):
    result_sets = {
        '30_90_dtw.txt': ChengduResultsDTW
    }

    for filename, model in result_sets.items():
        filepath = os.path.join(directory_path, filename)
        if os.path.exists(filepath):
            print(f"Importing data from {filename} to {model.__name__} table...")
            import_data(filepath, model,ChengduData,ChengduQuery)

# def process_line1(line,XianData,XianQuery):
#     parts = line.strip().split(',')
#     query_instance, _ = XianQuery.objects.get_or_create(id=(int(parts[0])+1))
#     data_instance, _ = XianData.objects.get_or_create(id=(int(parts[1])+1))
#     return {
#         'queryid': query_instance,
#         'dataid': data_instance,
#         'start': int(parts[2]),
#         'end': int(parts[3]),
#         'score': float(parts[4])
#     }
#
# def import_data1(filepath, model,XianData,XianQuery, batch_size=15000):
#     with open(filepath, 'r') as file:
#         batch = []
#         for line in file:
#             data = process_line1(line,XianData,XianQuery)
#             batch.append(model(**data))
#
#             if len(batch) >= batch_size:
#                 with transaction.atomic():
#                     model.objects.bulk_create(batch)
#                 batch = []
#
#         if batch:  # 插入剩余的数据
#             with transaction.atomic():
#                 model.objects.bulk_create(batch)
#
# def batch_import1(directory_path):
#     result_sets = {
#         '30_90_dtw.txt': XianResultsDTW,
#         '30_90_edr.txt': XianResultsEDR,
#         '30_90_erp.txt': XianResultsERP
#     }
#
#     for filename, model in result_sets.items():
#         filepath = os.path.join(directory_path, filename)
#         if os.path.exists(filepath):
#             print(f"Importing data from {filename} to {model.__name__} table...")
#             import_data1(filepath, model,XianData,XianQuery)


directory_path = r'G:\work\cp_data\chengdu'
batch_import(directory_path)



