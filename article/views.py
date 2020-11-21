from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from article.models import Article
from article.serializers import ArticleDetailSerializer, ArticleListSerializer, \
    ContactRequestCreateSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 50


class ArticlesListView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    queryset = Article.objects.filter(active=True)
    pagination_class = StandardResultsSetPagination


class ArticleDetailView(generics.RetrieveAPIView):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()


class ContactRequestCreateView(generics.CreateAPIView):
    serializer_class = ContactRequestCreateSerializer
