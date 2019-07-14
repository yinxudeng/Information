"""information URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from information.crud import views as crud_views
from information.queries.views import Query
from information.pagination import views as pagination_views
from information.upload import views as upload_views
from information.download import views as download_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create/', crud_views.create),
    url(r'^read/', crud_views.read),
    url(r'^update/', crud_views.update),
    url(r'^delete/', crud_views.delete),
    url(r'^query/', Query.as_view()),
    url(r'^pagination/', pagination_views.show_page),
    url(r'^upload/', upload_views.upload),
    url(r'^download/', download_views.export_excel),
]