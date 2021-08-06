from django.urls import path
from .import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView, UserPostListView



urlpatterns = [
        path('', PostListView.as_view(), name='blog-home'), #class based view
        path('user/<str:username>', UserPostListView.as_view(), name='user-post'),

        path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
        path('post/new/', PostCreateView.as_view(), name='create'),
        path('profile/post/new/', PostCreateView.as_view(), name='post-create'),
        path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
        path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
        #pk==primary key

        path('about/', views.about, name='blog-about'),

        path('like/<int:pk>/', views.like_post, name = 'like_post'),
        path('post/<int:pk>/comment/', views.CommentView.as_view(), name = 'add_comment'),
        path('comment-delete/<int:pk>/', views.CommentDeleteView.as_view(), name='comment_delete'),

]
