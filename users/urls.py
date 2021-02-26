from django.urls import path
from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.views import RegisterView
from .views import UserList, UserDetail

app_name = 'users'

urlpatterns = [
    path('users/', UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='sign_up')
]
