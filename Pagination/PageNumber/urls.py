from django.urls import path
from . import views
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns=[
    path("get_movie/",views.get_movie,name="get_movie"),
    path("get_movies_list/",views.get_movies_list,name="get_movies_list"),
    path("login_view/",views.login_view,name="login_view"),
    path("createUser/",views.createUser,name="createUser"),
    path("MovieListCreateView/",MovieListCreateView.as_view()),
    path("MovieRetrieveUpdateDestroyView/<int:pk>/",MovieRetrieveUpdateDestroyView.as_view()),
    path("post_form/",views.post_form,name="post_form"),
    path("get_user/",views.get_user,name="get_user"),
    path("login_page/",views.login_page,name="login_page"),
    path("logout_view/",views.logout_view,name="logout_view"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/protect/',protected_view, name='protect'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]