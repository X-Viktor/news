from django.urls import path

from news.views import (
    TypesAPIView, NewsAPIView, TypeDetailAPIView, NewsDetailAPIView
)

urlpatterns = [
    path('news/', NewsAPIView.as_view(), name='news'),
    path('types/', TypesAPIView.as_view(), name='types'),
    path('news/<slug:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('types/<slug:pk>/', TypeDetailAPIView.as_view(), name='type-detail'),
]
