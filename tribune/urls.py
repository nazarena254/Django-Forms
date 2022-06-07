"""tribune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# django.conf.urls.url() was deprecated in Django 3.0, and is removed in Django 4.0+.
# The easiest fix is to replace url() with re_path() or path() & import it from django.urls
# path() requires no regular expression unlike re_path()
from django.contrib import admin
from django.contrib.auth import views
from django.urls import re_path,path, include
# from django.conf.urls import url, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('tinymce/', include('tinymce.urls')), # it is rich text editor for users to write posts

    #django-registration provides the registration form and requires templates 
    # to be stored in a template subfolder called registration
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),

    # next_page defines the page to go to after the user is logged out
    # path('logout/',views.logout, {"next_page":'/'}), 

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
