from django.urls import path
from accounts.views import HomePageView, SignUpView, LoginView, IQroomView, SearchView, SignUpProView
from .views import PostView, All_posts


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('signup/', SignUpView, name='signup'),
    path('login/', LoginView, name='login'),
    path('iqfeed/', All_posts, name='iqfeed'),
    path('iqroom/', IQroomView.as_view(), name='iqroom'),
    path('search/', SearchView.as_view(), name='search'),
    path('signuppro/', SignUpProView, name='signuppro'),
    path('new/', PostView, name='new'),



]
