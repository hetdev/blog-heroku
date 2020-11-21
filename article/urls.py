from django.urls import path

from article.views import ArticleDetailView, ArticlesListView

urlpatterns = [
    path('article/list', ArticlesListView.as_view(),
         name="articles-list"),
    path('article/detail/<slug:slug>/<int:pk>', ArticleDetailView.as_view(),
         name="fair-project-listing"),
    # path('listing/fair-project-listing-fr-code/<int:fr_code>', ListingProjectsFrCodeView.as_view(),
    #      name="fair-project-listing-fr-code"),
]
