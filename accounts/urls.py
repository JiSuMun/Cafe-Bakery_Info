from django.urls import path
from . import views
# from .views import LoginView


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    # path('login-api/', LoginView.as_view(), name='login_api'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('profile/<username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('<int:user_pk>/follower/', views.follower, name='follower'),
]
