"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from posts.views import test_view, html_view, list_view, post_detail_view, create_post_view
from users.views import login_view, logut, register_view
from django.conf import settings
from django.conf.urls.static import static

users_paterns = [
    path('register/', register_view), # type: ignore
    path('login/', login_view), # type: ignore
    path('logout/', logut),
    ]

urlpatterns = users_paterns + [
    path('admin/', admin.site.urls),
    path("", html_view),
    path("list_view/", list_view), # type: ignore
    path("list_view/<int:post_id>", post_detail_view), # type: ignore
    path("list_view/create/", create_post_view), # type: ignore
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
