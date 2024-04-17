from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apiapp import views

urlpatterns = [
    path("apiapp/", views.Appuserlist.as_view()),
    path("users/<int:pk>/", views.Appuserdetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)