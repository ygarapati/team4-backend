from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

# @csrf_exempt
# @require_POST
# def loginPage(request):
#     request_body = json.loads(request.body)
#     authenticated = authenticate(username = request_body['username'],password = request_body['password'])
#     if authenticated:
#         login(request,authenticated)
#         return JsonResponse({"authenticated":True})
#     else:
#         return JsonResponse({"authenticated":False})


@csrf_exempt
@require_POST
def register_user(request):
    request_body = json.loads(request.body)
    username = request_body['username']
    password = request_body['password']
    email = request_body["email"]
    owner = User.objects.create_user(username = username, password = password,email = email)
    owner.save()
    return JsonResponse({"sucess":True})


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)