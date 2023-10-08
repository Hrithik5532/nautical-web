from django.urls import path
from .views import *

urlpatterns = [
        path("",home,name="home"),
        path("Services",services,name="services"),
        path("Contact-us",contact_us,name="contact_us"),
        path("Articles",articles_view,name="articles"),
        path("Article/(?P<slug>[-a-zA-Z0-9_]+)\\Z",article_details,name="article_details"),
        
]