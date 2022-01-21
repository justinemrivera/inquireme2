from django.urls import path
from accounts.views import SignUpView, IQroomView, SearchView, SignUpProView,  HomePageView, PostView, All_posts, LoginView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView, name='signup'),
    path('login/', LoginView, name='login'),
    path('iqfeed/', All_posts, name='iqfeed'),
    path('iqroom/', IQroomView.as_view(), name='iqroom'),
    path('search/', SearchView.as_view(), name='search'),
    path('signuppro/', SignUpProView, name='signuppro'),
    path('new/', PostView, name='new'),

]
