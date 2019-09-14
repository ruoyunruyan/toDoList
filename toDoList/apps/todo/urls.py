from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    re_path('edit/(?P<id>\d+)/$', views.EditView.as_view(), name='edit'),
    re_path('line/(?P<id>\d+)/$', views.LineThrough.as_view(), name='line'),
]
