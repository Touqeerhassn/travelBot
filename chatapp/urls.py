from django.urls import path

from .views import chat_api

urlpatterns = [
    path('', chat_api, name='chat-api'),
]