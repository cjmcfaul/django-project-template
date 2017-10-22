from django.conf.urls import url
from {{ project_name }}_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
