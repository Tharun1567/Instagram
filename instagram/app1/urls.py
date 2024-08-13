from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.home,name="homepage"),
    path("book",views.bookView,name="bookpage"),
    path("author",views.authorView,name="authorpage")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)