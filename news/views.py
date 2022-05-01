from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from news.models import Type, News
from news.serializer import (
    TypeSerializer, NewsSerializer, NewsDetailSerializer
)


class TypesAPIView(ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class NewsAPIView(ListCreateAPIView):
    queryset = News.objects.select_related('type')
    serializer_class = NewsSerializer

    def get_queryset(self):
        type_name = self.request.GET.get('type', '')
        if type_name:
            return self.queryset.filter(type__name=type_name)
        return self.queryset.all()


class TypeDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class NewsDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.select_related('type')
    serializer_class = NewsDetailSerializer
