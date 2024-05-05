from django.shortcuts import render
from .models import Item, AboutPage
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView

def index(request):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(Item.objects.all().order_by('created_at'), 3)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'core/index.html', context=context)

def about_view(request):
    about_content = AboutPage.objects.first()  # assumes there is at least one entry
    context = {'about_content': about_content}
    return render(request, 'core/about.html', context=context)

class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/item_detail.html'