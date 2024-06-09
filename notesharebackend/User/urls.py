from django.urls import path
from .views import UserViewSet, UserRegisterView, AllUsersView, UserLoginView

urlpatterns = [
    path('get_user/', UserViewSet.as_view()),
    path('signup/', UserRegisterView.as_view(), name='register'),
    path('all_users/', AllUsersView.as_view(), name='all_users'),
    path('login/', UserLoginView.as_view(), name='login')
]