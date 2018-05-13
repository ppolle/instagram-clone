from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^accounts/profile',views.profile,name = 'profile'),
    url(r'^accounts/create',views.create,name = 'create'),
     url(r'^accounts/search',views.search,name = 'search'),
    url(r'^accounts/updateProfile',views.updateProfile,name = 'updateProfile'),
    url(r'^accounts/single/(\d+)',views.single,name = 'single')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)