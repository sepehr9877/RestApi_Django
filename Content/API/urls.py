from django.urls import path
from .views import GetAllContentView,UpdateContent
urlpatterns=[
    path('GetAllContent',GetAllContentView.as_view()),
    path('Update_Content/<int:id>',UpdateContent.as_view())
]
