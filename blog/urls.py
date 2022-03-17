from django.urls import path

from blog.views import PostListView

urlpatterns=[
    path("", PostListView.as_view()),
    # path("<category>/", QuizView.as_view()),
    # path("<category>/<quiz>/", QuestionView.as_view())
    ]