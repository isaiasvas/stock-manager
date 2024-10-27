from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API de Gestão de Estoque",
        default_version='v1.1',
        description="Documentação da API de Gestão de Clientes, Fornecedores, Produtos e Movimentação de Estoque",
        terms_of_service="https://www.seusite.com/termos/",
        contact=openapi.Contact(email="isaias@visioit.com.br"),
        license=openapi.License(name="Licença MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Permite acesso público à documentação
)

schema_view.security = [
    {
        'Bearer': [],
    }
]

schema_view.securityDefinitions = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Insira seu token JWT com o prefixo 'Bearer '",
    }
}

# Defina o esquema de segurança para autenticação JWT
schema_view.authentication = [
    openapi.Parameter(
        'Authorization',
        openapi.IN_HEADER,
        description="Insira seu token JWT com o prefixo 'Bearer '",
        type=openapi.TYPE_STRING,
        required=True,
    ),
]

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Incluindo as URLs do seu aplicativo
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Rota para obter o token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Rota para refrescar o token
]
