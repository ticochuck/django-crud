
from django.urls import include, path

from .views import CreatePageView, DeletePageView, DetailPageView, HomePageView, UpdatePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create/', CreatePageView.as_view(), name='create'),
    path('detail_view/<int:pk>', DetailPageView.as_view(), name='detail_view'),
    path('update/<int:pk>', UpdatePageView.as_view(), name='update'),
    path('delete/<int:pk>', DeletePageView.as_view(), name='delete'),
]
