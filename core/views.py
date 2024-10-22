from django.shortcuts import render
from .models import Item, AboutPage
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView

def rearrange_items(items):
    n = len(items)
    center = (n - 1) // 2
    result = []
    for i in range(n):
        if i % 2 == 0:
            index = center + (i // 2)
        else:
            index = center - ((i + 1) // 2)
        result.append(items[index])
    return result


def index(request):
    # Fetch your items as usual
    items = Item.objects.all()
    # Rearrange items
    rearranged_items = rearrange_items(list(items))
    # Paginate if necessary
    paginator = Paginator(rearranged_items, per_page=10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/index.html', {'page_obj': page_obj})


def about_view(request):
    about_content = AboutPage.objects.first()  # assumes there is at least one entry
    context = {'about_content': about_content}
    return render(request, 'core/about.html', context=context)

class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/item_detail.html'