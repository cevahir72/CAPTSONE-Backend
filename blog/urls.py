from django.urls import path

from blog.views import ( PostListView,DetailView,CommentView,LikeView,PostViewList)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:id>/', DetailView.as_view(), name='post-detail'),
    path('<int:id>/comment/', CommentView.as_view()),
    path('<int:id>/like/', LikeView.as_view()),
    path('<int:id>/view/', PostViewList.as_view()),
]