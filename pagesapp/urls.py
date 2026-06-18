from django.urls import path
from .views import HomePageView , AboutPageView ,SardorPageView ,BasePageView
urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('about',AboutPageView.as_view(), name='about'),
    path('sardor',SardorPageView.as_view(), name='sardor'),
    path('base',BasePageView.as_view(), name='base'),
]