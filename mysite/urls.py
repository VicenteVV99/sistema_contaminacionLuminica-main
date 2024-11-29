from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    # path('mediciones/', include('historialMediciones.urls')),
    path('', include('fiscalizacion.urls')),
    path('', include('mediciones.urls')),
    path('', include('proyectos.urls')),
    path('', include('proyectosApi.urls')),
    path('', include('fiscalizacionApi.urls')),
    path('', include('medicionesApi.urls')),
    path('usuarios/', include('usuarios.urls')),  # Incluye las URLs de usuarios
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)