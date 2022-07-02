from django.urls import path 
# from .views import article_list_create_view,article_detail_view
from .views import ArticleDetailAPIView,ArticleListCreateAPIView, JournalistListCreateAPIView,JournalistDetailAPIView

urlpatterns = [
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>', ArticleDetailAPIView.as_view(), name='article-detail'),
    path('journalists/', JournalistListCreateAPIView.as_view(), name='journalist-list'),
    path('journalists/<int:pk>', JournalistDetailAPIView.as_view(), name='journalist-detail'),
    
    # path('articles/', article_list_create_view, name='article-list'),
    # path('articles/<int:pk>', article_detail_view, name='article-detail')

]