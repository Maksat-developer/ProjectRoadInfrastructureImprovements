from django.urls import path
from .views import *

urlpatterns = [

    path('message-list-create/',MessageModelListCreate.as_view()),
    path('message-delete/<int:pk>/',MessageModelDelete.as_view()),
    path('message-update/<int:pk>/',MessageModelUpdate.as_view()),

]
