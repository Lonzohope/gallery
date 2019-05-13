from django.conf.urls import url
from . import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns=[
    url(r'^$',views.photo_today,name='PhotoToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photo,name = 'pastPhoto'),
    url(r'^search/', views.search_results, name='search_results')
    
]
   


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
