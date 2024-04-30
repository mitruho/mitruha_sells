from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('items/<pk>', views.ItemDetailView.as_view(), name='item_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)