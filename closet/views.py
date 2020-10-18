from django.shortcuts import render
from django.views.generic import ListView, DetailView
from closet.models import Closet
from django.views.generic import FormView
from closet.forms import ClothesSearchForm
from django.db.models import Q
from closet.models import Closet


# Create your views here.
class ClosetLV(ListView):
    model = Closet
    paginate_by = 9


class ClosetDV(DetailView):
    model = Closet


class SearchFormView(FormView):
    form_class = ClothesSearchForm
    template_name = 'closet/closet_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        clothes_list = Closet.objects.filter(Q(brand__icontains=searchWord) | Q(classification__icontains=searchWord) | Q(product_name__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = clothes_list

        return render(self.request, self.template_name, context)
