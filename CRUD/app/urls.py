from django.urls import path
from .views import Student_retrieve, delete_view, update_view, StudentRegistrationView, signin_view, logout_view

urlpatterns = [
    path("s", Student_retrieve, name="retrieve"),
    path("dl/<int:pk>/", delete_view, name="delete_url"),
    path("up/<int:pk>/", update_view, name="update_url"),
    path("signup", StudentRegistrationView.as_view(), name="signupview" ),
    path("lg", signin_view, name="login"),
    path('logout/', logout_view, name='logout'),
    
]
