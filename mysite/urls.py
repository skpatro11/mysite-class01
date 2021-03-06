from django.contrib import admin
from django.urls import path, include
from .views import index, contact_us, about_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contact_us/', contact_us),
    path('about_us/', about_us),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
]
