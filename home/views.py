from rest_framework import viewsets, filters
from django.views.generic import TemplateView
from .models import Mot, Synonyme, Antonyme, Expression
from .serializers import MotSerializer, SynonymeSerializer, AntonymeSerializer, ExpressionSerializer

class Index(TemplateView):
    template_name = 'search.html'
class MotViewSet(viewsets.ModelViewSet):
    queryset = Mot.objects.all()
    serializer_class = MotSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['mot', 'description', 'categorie']

class SynonymeViewSet(viewsets.ModelViewSet):
    queryset = Synonyme.objects.all()
    serializer_class = SynonymeSerializer

class AntonymeViewSet(viewsets.ModelViewSet):
    queryset = Antonyme.objects.all()
    serializer_class = AntonymeSerializer

class ExpressionViewSet(viewsets.ModelViewSet):
    queryset = Expression.objects.all()
    serializer_class = ExpressionSerializer

class MotViewSet(viewsets.ModelViewSet):
    queryset = Mot.objects.all()
    serializer_class = MotSerializer

