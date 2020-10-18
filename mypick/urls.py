from django.urls import path
from mypick.views import MypickLV, MypickDV

app_name = 'mypick'
urlpatterns = [
    path('', MypickLV.as_view(), name='index'),
    path('<int:pk>/', MypickDV.as_view(), name='detail'),
]