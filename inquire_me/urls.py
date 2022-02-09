"""inquireme2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
# from .views import IqUpdateView, upload_file
from django.conf import settings
from django.conf.urls.static import static


# from accounts.views import All_categories
from .views import (IqUpdateView, IqDeleteView,
                    PostDetailView, CategoryDetailView, cat)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('category/<str:cats>/', CategoryDetailView, name='post_category'),
    path('feed/<int:pk>/edit', IqUpdateView.as_view(), name='edit_post'),
    path('feed/<int:pk>/delete', IqDeleteView.as_view(), name='delete_post'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('', cat, name='home'),
    # path('home/', All_categories, name='home'),




    # path('signuppro/', upload_file, name='signuppro')




]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
