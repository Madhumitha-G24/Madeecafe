from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cafe.urls')),  # ✅ This is the correct way to include the app's URLs
]
