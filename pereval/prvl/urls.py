from django.urls import path

from .views import PerevalApiView


urlpatterns = [
    path('submitData/', PerevalApiView.as_view(), name='submit_data')
]