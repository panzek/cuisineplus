from django.urls import path
from home.views import Home


# urlpatterns = [
#     path('', HomePageView.as_view(), name='Home'),
# ]

urlpatterns = [
    path('', Home, name='Home'),
]