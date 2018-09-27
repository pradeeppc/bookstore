from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .forms import AuthenticationForm
from django.conf import settings
from django.views.generic.base import RedirectView




urlpatterns = [
    path(r'', views.index, name='index'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('accounts/logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    path(r'accounts/signup/', views.signup, name='signup'),
    path(r'games-list/highlighted/', views.show_highlighted_games),
    path(r'games-list/all/', views.show_all_games),
    path(r'cart/', views.ShoppingCartEditView.as_view(), name='user-cart'),
    path(r'cart/add/<int:game_id>/', views.add_to_cart),
    path(r'cart/send', views.send_cart),
    path(r'my-orders/', views.my_orders),
    path(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon/favicon.ico')),
]