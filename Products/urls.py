from django.urls import path
from .views import ProductDetail,ProductPage,ProdetailMixin,ProMixin,UserDetail,UserList
urlpatterns=[
    path('Products',ProMixin.as_view()),
    path('Products/<int:pk>',ProdetailMixin.as_view()),
    path('User',UserList.as_view()),
    path('User/<int:pk>',UserDetail.as_view())

]