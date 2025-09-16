from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('' , views.index, name='home'),
    path('add_room/', views.add_room, name='add_room'), 
    path('admin', admin.site.urls),
    path('about/', views.about, name='about'),
    path('room/<int:pk>/', views.room_detail_view, name='room_detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
