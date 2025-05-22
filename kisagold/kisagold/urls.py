from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # mount app dashboard di URL /dashboard/
    path('dashboard/', include('dashboard.urls')),

    path('admin/', admin.site.urls),
]
