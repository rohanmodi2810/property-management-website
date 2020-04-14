"""property_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import view

urlpatterns = [
    path('',view.about,name='home'),
    path('login_owner/',view.login_owner,name='login_owner'),
    path('login_buyer/',view.login_buyer,name='login_buyer'),
    path('loginpage_buyer/',view.loginpage_buyer,name='loginpage_buyer'),
    path('loginpage_owner/',view.loginpage_owner,name='loginpage_owner'),
    path('register_buyer/',view.register_buyer,name='register_buyer'),
    path('register_seller/',view.register_seller,name='register_seller'),
    path('temp/',view.temp,name='temp'),
    path('admin/', admin.site.urls),
    path('seller_info/',view.seller_info,name='seller_info'),
    path('buyer_info/',view.buyer_info,name='buyer_info'),
    path('customer_history/',view.customer_history,name='customer_home'),
    path('owner_history/',view.owner_history,name='customer_home'),

    path('add/',view.add, name="add"),
    path('update/',view.update, name="update"),
    path('delete/',view.delete, name="delete"),
    path('myProperty/',view.myProperty, name="myProperty"),
    path('view_this/<int:id>',view.view_this, name="view_this"),
    path('delete_this/<int:id>',view.delete_this, name="delete_this"),
    path('update_this/<int:id>',view.update_this, name="update_this"),
    path('update_id/<int:id>',view.update_id, name="update_id"),
    path('add_property/', view.add_property, name="add_property"),

    path('search_property/',view.search_property,name='serch_property'),
    path('done_buy/<int:p_id>/',view.done_buy,name="done_buy"),
    path('buyer_history/',view.buyer_history,name="buyer_history"),

    path('go_to_owner_home/',view.go_to_owner_home,name='go_to_owner_home'),
    path('go_to_customer_home/',view.go_to_customer_home,name='go_to_customer_home'),

    path('log_in_page_buyer/',view.log_in_page_buyer,name='log_in_page_buyer'),
    path('log_in_page_owner/',view.log_in_page_owner,name='log_in_page_buyer'),

    path('signup_buyer/',view.signup_buyer,name='signup_buyer'),
    path('signup_owner/',view.signup_owner,name='signup_owner'),

    path('ContactUs/',view.ContactUs,name="ContactUs"),
    path('AboutUs/',view.AboutUs,name="AbouttUs"),

    path('get_price/',view.getPrice,name="get_price"),
    path('predictPrice/',view.predictPrice, name="predictPrice")

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)