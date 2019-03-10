from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogposts/', views.BlogPostListView.as_view(), name='blogposts'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('blogpost/<int:pk>', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('comment/<int:pk>', views.Comment.as_view(), name='comments'),
    path(r'blogpost/<int:pk>/comment/', views.add_comment_to_post, name='add-comment-to-post'),
]