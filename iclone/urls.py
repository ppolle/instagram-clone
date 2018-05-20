from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^timeline/$',views.timeline,name = 'timeline'),
    url(r'^accounts/profile/(\d+)',views.profile,name = 'profile'),
    url(r'^accounts/create',views.create,name = 'create'),
     url(r'^accounts/search',views.search,name = 'search'),
    url(r'^accounts/updateProfile',views.updateProfile,name = 'updateProfile'),
    url(r'^accounts/single/(\d+)',views.single,name = 'single'),
    url(r'^like/(\d+)',views.likePost,name= 'likePost'),
	url(r'^follow/(\d+)',views.follow,name="user_follow"),
	url(r'^editPost/(\d+)',views.editPost,name="editPost"),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)