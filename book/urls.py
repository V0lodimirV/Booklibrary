"""
URL configuration for book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from lib_book import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("reader/<int:reader_id>/", views.reader_detail, name="reader_detail"),
    path("reader/<int:reader_id>/borrow/", views.borrow_book, name="borrow_book"),
    path("reader/<int:reader_id>/return/", views.return_book, name="return_book"),
    path("reader/<int:reader_id>/book_detail/", views.book_detail, name="book_detail"),
    path(
        "reader/<int:reader_id>/return_detail/",
        views.return_detail,
        name="return_detail",
    ),
]
