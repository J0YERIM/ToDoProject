from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),
    path('calendar/', include('todolist.urls')),
    path('profile/', include('users.urls')),
]
