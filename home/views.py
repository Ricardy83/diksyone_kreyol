from django.shortcuts import render
from .models import DictionaryEntry

def search(request):
    query = request.GET.get('q')
    results = DictionaryEntry.objects.filter(word__icontains=query) if query else None
    return render(request, 'search.html', {'results': results, 'query': query})
