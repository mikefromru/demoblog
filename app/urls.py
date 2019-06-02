from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='index'),
    path('detail/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
]