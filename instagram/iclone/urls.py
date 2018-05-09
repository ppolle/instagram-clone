from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^accounts/profile',views.profile,name = 'profile'),
    
]