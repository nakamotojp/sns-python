from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

URLPattern = [
    path('', views.index, name='index'),
    path('<int:page>', views.index, name='index'),
    path('groups', views.groups, name='grouos'),
    path('add', views.add, name='add'),
    path('creategroup', views.creategroup, name='creategroup'),
    path('post', views.post, name='post'),
    path('share/<int:share_id>', views.share, name='share'),
    path('good/<int:good_id>', views.good, name='good'),
]