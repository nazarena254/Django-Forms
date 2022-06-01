from django.urls import re_path, include
from . import views
# from django.conf.urls import url

urlpatterns=[   

    re_path(r'^$',views.news_today,name='newsToday'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^article/(\d+)',views.article,name ='article')   
     
]