from django.shortcuts import render
from django.http import HttpResponse,request,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from aipocapi.models import robo
from .serializers import ItemSerializer

@csrf_exempt
def item_list(request):
    if request.method == 'GET':
        items = item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)


@csrf_exempt
def item_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        items = item.objects.get(id=pk)
    except item.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(items)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(items, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        items.delete()
        return HttpResponse(status=204)
