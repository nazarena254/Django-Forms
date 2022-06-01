from django.urls import re_path,path, include
from . import views
# from django.conf.urls import url

urlpatterns=[   

    path('',views.news_today,name='newsToday'),
    path('archives/',views.past_days_news,name = 'pastNews'),
    path('search/', views.search_results, name='search_results'),
    path('article/',views.article,name ='article')   
     
]