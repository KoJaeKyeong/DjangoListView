from django.urls import path
from closet.views import ClosetLV, ClosetDV, SearchFormView


app_name = 'closet'
urlpatterns = [
    path('', ClosetLV.as_view(), name='index'),
    path('<int:pk>/', ClosetDV.as_view(), name='detail'),
    path('search/', SearchFormView.as_view(), name='search'),
]