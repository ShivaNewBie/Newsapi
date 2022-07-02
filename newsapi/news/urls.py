from django.urls import path 
# from .views import article_list_create_view,article_detail_view
from .views import ArticleDetailAPIView,ArticleListCreateAPIView

urlpatterns = [
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>', ArticleDetailAPIView.as_view(   ), name='article-detail'),
    # path('articles/', article_list_create_view, name='article-list'),
    # path('articles/<int:pk>', article_detail_view, name='article-detail')

]