from django.urls import path
from .views import PostList, PostDetail, PostAdd, PostUpdateView, PostDeleteView





urlpatterns = [
        path('', PostList.as_view()),
        path('<int:pk>', PostDetail.as_view(), name='post_detail'),
        path('<int:pk>', PostDetail.as_view(), name='post_detail'),
        path('add', PostAdd.as_view(), name='post_create'),
        path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
        path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]