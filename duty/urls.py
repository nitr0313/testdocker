from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('duty/', views.Generate.as_view(), name='generate'),
    path('duty/<str:date>', views.Generate.as_view(), name='generate'),
    path('duty/flat/create/',
         views.FlatCreate.as_view(), name='flat_create_url'),
    path('duty/flat/<int:id>/update/',
         views.FlatUpdate.as_view(), name='flat_update_url'),
    path('duty/flat/<int:id>/delete/',
         views.FlatDelete.as_view(), name='flat_delete_url'),
    path('duty/person/create/',
         views.PersonCreate.as_view(), name='person_create_url'),
    path('duty/person/<int:id>/update/',
         views.PersonUpdate.as_view(), name='person_update_url'),


]

# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
