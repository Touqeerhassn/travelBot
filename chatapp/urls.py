from django.urls import path

# from .views import chat_api
# from .views import add_passenger
# from .views import all_passenger
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.chat_api, name='chat-api'),
] 
