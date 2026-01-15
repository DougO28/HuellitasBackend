from django.contrib import admin
from django.urls import path, include
from django.conf import settings               
from django.conf.urls.static import static
from django.shortcuts import redirect  # ← Agregar esto

# Función para redirigir al admin
def redirect_to_admin(request):
    return redirect('/admin/')

urlpatterns = [
    # Redirige la raíz al admin
    path('', redirect_to_admin, name='home'),  # ← Cambiar esto
    
    # Django Admin
    path('admin/', admin.site.urls),
    
    # API Routes
    path('api/auth/', include('apps.authentication.urls')),
    path('api/', include('apps.pets.urls')),
    path('api/adoptions/', include('apps.adoptions.urls')),
    path('api/contact/', include('apps.contact.urls')),
    path('api/content/', include('apps.content.urls')),
    path('api/', include('apps.common.urls')),
]

# Solo para archivos estáticos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)