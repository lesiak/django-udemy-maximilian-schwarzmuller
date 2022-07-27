from django.urls import path

from challenges.views import january, february

urlpatterns = [
    path('january', january),
    path('february', february)
]
