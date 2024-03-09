from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from produto.views import ProdutoView, ImportarArquivoView


router = SimpleRouter(trailing_slash=False)
router.register('produto', ProdutoView, basename='produtos')

urlpatterns = [
    path('', include(router.urls)),
    path('importar', ImportarArquivoView.as_view())
] + router.urls

urlpatterns = format_suffix_patterns(urlpatterns)
