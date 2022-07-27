"""superlists URL Configuration

The `urlpatterns` list routes URLs to list_views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function list_views
    1. Add an import:  from my_app import list_views
    2. Add a URL to urlpatterns:  url(r'^$', list_views.home, name='home')
Class-based list_views
    1. Add an import:  from other_app.list_views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from lists import views as list_views
from lists import urls as list_urls


urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/', include(list_urls)),
    url(r'^admin/', admin.site.urls),
]
