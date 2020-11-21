from django.urls import path

from article.views import ArticleDetailView, ArticlesListView, \
    ContactRequestCreateView

urlpatterns = [
    path('contact-request/create', ContactRequestCreateView.as_view(),
         name="contact-request-create"),
    path('article/list', ArticlesListView.as_view(),
         name="articles-list"),
    path('article/detail/<slug:slug>/<int:pk>', ArticleDetailView.as_view(),
         name="article-detail"),
]
