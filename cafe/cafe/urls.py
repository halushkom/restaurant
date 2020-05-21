"""cafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from article.views import IndexView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView #, DisplayView
from order.views import OrderView, OrderCreateView, OrderDetailView, OrderUpdateView, OrderDeleteView
from about_us.views import AboutView
from contact_us.views import contactView
from account.views import ProfileDetailView, SignUP
from menu.views import MenuView, MealList



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    #Article
    path('article/create', ArticleCreateView.as_view(), name='create'),
    #path('news-and-events', DisplayView.as_view(), name='news-and-events'),
    path('article/<int:article_id>', ArticleDetailView.as_view(), name='detail'),
    path('article/update/<int:article_id>', ArticleUpdateView.as_view(), name='update'),
    path('article/delete/<int:article_id>', ArticleDeleteView.as_view(), name='delete'),
    #Account
    path('account/profile/<int:profile_id>', ProfileDetailView.as_view(), name='profile'),
    path('account/', include('django.contrib.auth.urls')),
    path('signup/', SignUP.as_view(), name='signup'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    #Making order
    path('order/', OrderView.as_view(), name="order.html"),
    path('reservation', OrderCreateView.as_view(), name="reservation"),
    path('order/<int:order_id>', OrderDetailView.as_view(), name="order_detail"),
    path('order/update/<int:order_id>', OrderUpdateView.as_view(), name='order_update'),
    path('order/delete/<int:order_id>', OrderDeleteView.as_view(), name='order_delete'),
    #About us
    path('about-us', AboutView.as_view(), name="about-us"),
    #Contact us
    path('contact-us', contactView.as_view(), name="contact-us"),
    #Menu
    path('<slug:slug>/', MealList.as_view(), name="menu"),
    path('menu', MenuView.as_view(), name="menu"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
