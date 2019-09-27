from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiver/', include('quiver.urls')),
    path('', include('quiver.urls')),
]
