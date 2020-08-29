
from django.urls import include, path

from .views import CreatePageView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create/', CreatePageView.as_view(), name='create')
]
