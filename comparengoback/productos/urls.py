from django.urls import re_path, include

from .router import router

urlpatterns = [
    re_path(r'', include(router.urls)),
]