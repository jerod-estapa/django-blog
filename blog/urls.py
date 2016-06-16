# blog - urls.py

from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w|\-]+)$', views.post, name='post'),
    url(r'^add_post/', views.add_post, name='add_post'),
]