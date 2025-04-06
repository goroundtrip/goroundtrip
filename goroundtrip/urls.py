from django.contrib import admin
from django.urls import path, include  # ← added 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('flights/', include('flights.urls')), # ← add this line
]

