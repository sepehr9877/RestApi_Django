from django.urls import path
from .views import AccountUserList,RegisterAccount
urlpatterns=[
    path('AccountApi',AccountUserList.as_view()),
    path('Register',RegisterAccount.as_view())
]