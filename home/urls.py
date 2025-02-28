from django.urls import path, include
from home.views import *
from rest_framework.routers import DefaultRouter
from home.views import *

router = DefaultRouter()
router.register(r'mots', MotViewSet)
router.register(r'synonymes', SynonymeViewSet)
router.register(r'antonymes', AntonymeViewSet)
router.register(r'expressions', ExpressionViewSet)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('api/', include(router.urls)),
]
