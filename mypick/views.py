from django.shortcuts import render
from django.views.generic import ListView, DetailView
from mypick.models import Mypick


# Create your views here.
class MypickLV(ListView):
    model = Mypick
    paginate_by = 1


class MypickDV(DetailView):
    model = Mypick
