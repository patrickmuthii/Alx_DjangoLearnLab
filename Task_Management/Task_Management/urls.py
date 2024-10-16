"""
URL configuration for Task_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg import openapi


schema_view = swagger_get_schema_view(
   openapi.Info(
      title="Task_Management API",
      default_version='v1',
      description="API documentation of app",
      
   ),
   public=True,
  
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line
    path('', lambda request: redirect('task/')),
    path('api/v1/',
        include([ 
            path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-schema'),
            path('task/', include('Task.urls')),



])
        )
]
