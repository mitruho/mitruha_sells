from django.shortcuts import render
from .models import Item
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView

def index(request):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(Item.objects.all().order_by('created_at'), 3)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'core/index.html', context=context)

def about(request):
    return render(request, 'core/about.html')

class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/item_detail.html'