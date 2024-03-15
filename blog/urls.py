# from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("<int:pk>/<slug:slug>", views.PostView.as_view(), name="post"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("make-post/", views.make_a_post, name="post"),
    path("search/", views.SearchView.as_view(), name="search"),

#              del later + 1st line idk what i was
#                  tryin to fuckin do with this
#    path('login/', auth_views.LoginView.as_view(), name='login'),
#    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#    path('signup/', YourSignUpView.as_view(), name='signup'),
]
