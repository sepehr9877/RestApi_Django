from django.urls import path
from .views import AccountUserList
urlpatterns=[
    path('AccountApi',AccountUserList.as_view())
]