from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import json

api_view()
#@permission_classes([AllowAny])

@csrf_exempt
def get_car (request):
    
    topSpeed = 100
    carName = request.GET['car_name']
    topSpeed = request.GET['top_speed']
    response = { "GET": "The below data has been retrieved.", "car_name": carName, "top_speed": topSpeed }
    return JsonResponse( response )

@csrf_exempt
def post_car (request):
    carName = request.GET['car_name']
    topSpeed = request.GET['top_speed']
    response = { "POST": "The below data has been inserted.", "car_name": carName, "top_speed": topSpeed }
    return JsonResponse( response )

@csrf_exempt
def post_car_raw (request):    
    response = json.loads(request.body.decode('utf-8'))
    return JsonResponse( response )

@csrf_exempt
def post_car_form (request):  
    response = request.POST
    return JsonResponse( response )

@csrf_exempt
def del_car (request):
    carName = request.GET['car_name']
    topSpeed = request.GET['top_speed']
    response = { "DELETE": "The below data has been deleted.", "car_name": carName, "top_speed": topSpeed }
    return JsonResponse( response )

@csrf_exempt
def put_car (request):
    carName = request.GET['car_name']
    newSpeed = request.GET['new_speed']
    response = { "PUT": "The below data has been updated.", "car_name": carName, "top_speed": newSpeed }
    return JsonResponse( response )

@csrf_exempt
def patch_car (request):
    carName = request.GET['car_name']
    newSpeed = request.GET['new_speed']
    response = { "PATCH": "The below data has been updated.", "car_name": carName, "top_speed": newSpeed }
    return JsonResponse( response )