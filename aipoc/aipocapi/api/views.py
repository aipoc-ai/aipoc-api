from django.shortcuts import render
from django.http import HttpResponse,request,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from aipocapi.models import robo
from .serializers import ItemSerializer

@csrf_exempt
def item_list(request):
    if request.method == 'GET':
        items = robo.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = ItemSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def item_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        items = robo.objects.get(id=pk)
    except robo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(items)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = ItemSerializer(items, data=tutorial_data) 
        tutorial_serializer.save() 
        return JsonResponse(tutorial_serializer.data)
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        items.delete()
        return HttpResponse(status=204)
