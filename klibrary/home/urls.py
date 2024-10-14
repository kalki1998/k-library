from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('books/', views.books, name='books'),
    path('addbooks/', views.add, name='add'),
    path('edit/<pk>', views.edit, name='edit'),
    path('delete/<pk>', views.delete, name='delete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
