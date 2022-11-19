from django.urls import path
from .views import RegisterAccount,LoginPageRequest,GetAccountDetail
urlpatterns=[
    path('Register/',RegisterAccount.as_view()),
    path('LoginPage/',LoginPageRequest.as_view()),
    path('GetAccountDetail/',GetAccountDetail.as_view())
]