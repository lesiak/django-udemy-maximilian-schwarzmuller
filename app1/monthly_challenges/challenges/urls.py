from django.urls import path

from challenges.views import index

urlpatterns = [
    path('january', index)
]
