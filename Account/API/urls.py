from django.urls import path
from .views import RegisterAccount,LoginPageRequest,GetAccountDetail,UpdateDetail
urlpatterns=[
    path('Register/',RegisterAccount.as_view()),
    path('LoginPage/',LoginPageRequest.as_view()),
    path('GetAccountDetail/',GetAccountDetail.as_view()),
    path('UpdateUser/<int:id>',UpdateDetail.as_view())
]