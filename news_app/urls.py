from django.urls import path
from . import views
from .views import like_article
from .views import submit_article

urlpatterns = [
    path("", views.home, name="home"),
    path("articles/<int:id>/", views.article_detail, name="article_detail"),
    path("search/", views.search, name="search"),
    path('like/<int:article_id>/', like_article, name='like_article'),
    path("articles/<int:article_id>/comment/", views.add_comment, name="add_comment"),
    path("submit/", submit_article, name="submit_article"),
]


