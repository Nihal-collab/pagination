from django.shortcuts import render,redirect
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from .pagination import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from rest_framework import status
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer



@api_view(["GET"])
def get_movie(request):
    data=Movie.objects.all()
    paginator=Movie_Page()
    paginated_items=paginator.paginate_queryset(data,request)
    ser=Movie_Ser(paginated_items,many=True)
    return paginator.get_paginated_reponse(ser.data)
    
def get_movies_list(request):
    Movies=Movie.objects.all()
    paginator=Paginator(Movies,5)
    page_number = request.GET.get('page')  # get page number from query string
    page_obj = paginator.get_page(page_number)  # handles invalid page numbers gracefully
    return render(request, 'table.html', {'page_obj': page_obj})

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        # Authentication successful
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        # Authentication failed
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
def createUser(request):
    user = User.objects.create_user(
        username='Nihal123',
        email='nihalssss@gmail.com',
        password='securepassword123'
    )
    return JsonResponse({'message':{'user{user.username} created successfully'}})



class MovieListCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = Movie_Ser
    pagination_class = None  

class MovieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView ):
    queryset = Movie.objects.all()
    serializer_class = Movie_Ser
    pagination_class = None  



def post_form(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        print(username, email,password,confirm)
        CustomUser.objects.create_user(
            username = username,
            email=email,
            password=password,
            confirm=confirm

        )
        return redirect('get_user')
    else:
        return render(request,'form.html')

def get_user(request):
    data=CustomUser.objects.filter(is_superuser=False)
    context={'data':data}
    return render(request,"logindetails.html",context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        print('username',username)
        password = request.POST.get("password")
        print('password',password)

        user = authenticate(request, username=username, password=password)
        print('user',user)

        if user is not None:
            login(request, user)
            return redirect(get_user)  # or any dashboard page
        else:
            return HttpResponse("Invalid username or password.")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login_page")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': 'This is a protected view accessible only with a valid JWT.'})


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer