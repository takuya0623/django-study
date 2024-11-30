from django.contrib import admin
from django.urls import path
from word.views import frontpage, post_detail, create_item
from django.contrib.auth import views as auth_views
from word import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", frontpage),
    path("<slug:slug>/", post_detail, name="post_detail"),
    path("items/", create_item, name="create_item"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('accounts/logout/', views.logout_view, name="logout"),
    path('accounts/signup/', views.signup, name="signup"),
    path('accounts/profile/', views.profile, name="profile"),
]
