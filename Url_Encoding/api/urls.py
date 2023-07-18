from django.urls import path
from .views import EncodeURLView

app_name = 'api'

urlpatterns = [
    path('encode_url/', EncodeURLView.as_view(), name='encode_url'),
]
