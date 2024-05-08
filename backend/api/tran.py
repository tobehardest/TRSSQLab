import os
import json
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application =get_wsgi_application()

from api.models import ChengduData  # 替换为您的实际模型
from api.models import *

def process_file(filepath):
    with open(filepath, 'r') as file:
        return [{'lng': float(line.split()[0]), 'lat': float(line.split()[1])} for line in file]

def batch_import(directory_path, batch_size=1000):
    files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]
    batch = []
    if 'chengdu' in directory_path:
        i = 0
        while i < 30000:
            filepath = os.path.join(directory_path, str(i))
            coordinates = process_file(filepath)
            json_data = json.dumps(coordinates)
            batch.append(ChengduData(trajectory=json_data))
            if len(batch) >= batch_size:
                ChengduData.objects.bulk_create(batch)
                batch = []  # 清空批次列表以开始新的批次

            i += 1  # 自增i

        # 插入剩余的数据
        if batch:
            ChengduData.objects.bulk_create(batch)
    if 'porto' in directory_path:
        i = 0
        while i < 30000:
            filepath = os.path.join(directory_path, str(i))
            coordinates = process_file(filepath)
            json_data = json.dumps(coordinates)
            batch.append(PortoData(trajectory=json_data))
            if len(batch) >= batch_size:
                PortoData.objects.bulk_create(batch)
                batch = []  # 清空批次列表以开始新的批次

            i += 1  # 自增i
        # 插入剩余的数据
        if batch:
            PortoData.objects.bulk_create(batch)
    if 'xian' in directory_path:
        i = 0
        while i < 30000:
            filepath = os.path.join(directory_path, str(i))
            coordinates = process_file(filepath)
            json_data = json.dumps(coordinates)
            batch.append(XianData(trajectory=json_data))
            if len(batch) >= batch_size:
                XianData.objects.bulk_create(batch)
                batch = []  # 清空批次列表以开始新的批次

            i += 1  # 自增i
        # 插入剩余的数据
        if batch:
            XianData.objects.bulk_create(batch)

def batch_qimport(directory_path, batch_size=1000):
    files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]
    batch = []
    if 'chengdu' in directory_path:
        i = 0
        while i < 2000:
            filepath = os.path.join(directory_path, str(i))
            coordinates = process_file(filepath)
            json_data = json.dumps(coordinates)
            batch.append(ChengduQuery(trajectory=json_data))
            if len(batch) >= batch_size:
                ChengduQuery.objects.bulk_create(batch)
                batch = []  # 清空批次列表以开始新的批次

            i += 1  # 自增i

        # 插入剩余的数据
        if batch:
            ChengduQuery.objects.bulk_create(batch)
    if 'porto' in directory_path:
        i = 0
        while i < 2000:
            filepath = os.path.join(directory_path, str(i))
            coordinates = process_file(filepath)
            json_data = json.dumps(coordinates)
            batch.append(PortoQuery(trajectory=json_data))
            if len(batch) >= batch_size:
                PortoQuery.objects.bulk_create(batch)
                batch = []  # 清空批次列表以开始新的批次

            i += 1  # 自增i
        # 插入剩余的数据
        if batch:
            PortoQuery.objects.bulk_create(batch)
    if 'xian' in directory_path:
        i = 0
        while i < 2000:
            filepath = os.path.join(directory_path, str(i))
            coordinates = process_file(filepath)
            json_data = json.dumps(coordinates)
            batch.append(XianQuery(trajectory=json_data))
            if len(batch) >= batch_size:
                XianQuery.objects.bulk_create(batch)
                batch = []  # 清空批次列表以开始新的批次

            i += 1  # 自增i
        # 插入剩余的数据
        if batch:
            XianQuery.objects.bulk_create(batch)

directory_path = r'G:\work\cp_data\chengdu\all_tra_path_td_90_300'
directory_query_path = r'G:\work\cp_data\chengdu\all_tra_path_tq_30_89'
directory_path2 = r'G:\work\cp_data\porto\all_tra_path_td_90_300'
directory_query_path2 = r'G:\work\cp_data\porto\all_tra_path_tq_30_89'
directory_path3 = r'G:\work\cp_data\xian\all_tra_path_td_90_300'
directory_query_path3 = r'G:\work\cp_data\xian\all_tra_path_tq_30_89'
batch_import(directory_path)
batch_import(directory_path2)
batch_import(directory_path3)
batch_qimport(directory_query_path)
batch_qimport(directory_query_path2)
batch_qimport(directory_query_path3)



