"""moviescorner URL Configuration

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
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",views.SignUpView.as_view(),name="register"),
    path("login/",views.SignInView.as_view(),name="signin"),
    path("logout/",views.sign_out_view,name="signout"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("movie/add/",views.MovieCreateView.as_view(),name="movie-add"),
    path("movie/all/",views.MovieListView.as_view(),name="movie-list"),
    path("movie/<int:pk>/",views.MovieDetailsView.as_view(),name="movie-detail"),
    path("movie/<int:pk>/change/",views.MovieEditView.as_view(),name="movie-edit"),
    path("movie/<int:pk>/remove/",views.movie_delete_view,name="movie-delete"),
    # path("movie/<int:pk>/remove",views.MovieDeleteView.as_view(),name="movie-delete"),
    path("password/change/",views.PasswordResetView.as_view(),name="password-reset"),
    path("moviescorner/",views.HomeView.as_view(),name="movie")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
