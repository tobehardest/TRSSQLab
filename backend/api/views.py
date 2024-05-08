from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from api.models import *
from api.serializers import  *
import json

def get_top_results(request):
    city = request.GET.get('city')
    alg = request.GET.get('alg')
    query_id = request.GET.get('query_id')
    limit = int(request.GET.get('limit'))
    i=0
    print(city,alg)
    model_mapping = {
        'chengdu': {
            'dtw': (ChengduResultsDTW, ChengduResultsDTWSerializer,ChengduQuerySerializer),
            'edr': (ChengduResultsEDR, ChengduResultsEDRSerializer,ChengduQuerySerializer),
            'erp': (ChengduResultsERP, ChengduResultsERPSerializer,ChengduQuerySerializer),
        },
        'porto': {
            'dtw': (PortoResultsDTW, PortoResultsDTWSerializer,PortoQuerySerializer),
            'edr': (PortoResultsEDR, PortoResultsEDRSerializer,PortoQuerySerializer),
            'erp': (PortoResultsERP, PortoResultsERPSerializer,PortoQuerySerializer),
        },
        'xian': {
            'dtw': (XianResultsDTW, XianResultsDTWSerializer,XianQuerySerializer),
            'edr': (XianResultsEDR, XianResultsEDRSerializer,XianQuerySerializer),
            'erp': (XianResultsERP, XianResultsERPSerializer,XianQuerySerializer),
        }
    }
    print(query_id)
    model, serializer_class,serializer_class1 = model_mapping.get(city, {}).get(alg, (None, None))
    final_results = []
    querytrajectory=[]
    if not model or not serializer_class:
        return JsonResponse({'error': 'Invalid city or algorithm'}, status=400)

    queryset = model.objects.filter(queryid_id=query_id).order_by('-score')[:limit]
    print(queryset)
    tracjson = serializer_class1(queryset[0].queryid)
    querytrajectory.append(tracjson.data)
    # 使用外键直接访问轨迹数据
    for result in queryset:
        try:
            trajectory_data = json.loads(result.dataid.trajectory)
            trajectory_segment = trajectory_data[result.start:result.end+1]
            print(result.dataid_id,result.start,result.end,result.score)
            final_results.append(trajectory_segment)
        except AttributeError:
            continue  # 处理没有找到轨迹或字段不匹配的情况

    data={
        'querytrajectory':tracjson.data,
        'final_results':final_results
    }

    return JsonResponse(data, safe=False)
