from django.contrib import admin
from django.urls import path
from accounts.views import (LoginProView, log_in,
                            IQroomView, SearchView,  logout_view, signup, All_posts, PostView,
                            signuppro, LikeView)


urlpatterns = [

    path('iqroom/', IQroomView.as_view(), name='iqroom'),
    path('search/', SearchView.as_view(), name='search'),
    path('signuppro/', signuppro, name='signuppro'),
    path('login/', log_in, name='login'),
    path('signup/', signup, name='signup'),
    path('loggedout/', logout_view, name='logout'),
    path('iqfeed/', All_posts, name='feed'),
    path('new/', PostView, name='new'),
    path('like/<int:pk>', LikeView, name='home'),
    path('loginpro/', LoginProView, name='loginpro')
]
# path('like/<int:pk>', LikeView, name='like_post' ),
