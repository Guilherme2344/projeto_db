from django.shortcuts import render
from .models import ViewDb

def view_db(request):
    dados = ViewDb.objects.all()  # Busca todos os dados da view
    return render(request, template_name='index.html', context={'dados': dados})