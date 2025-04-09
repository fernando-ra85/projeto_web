from django.shortcuts import render
from datetime import datetime

# Create your views here.

def homepage(request):
    hora_atual = datetime.now().hour

    if hora_atual < 12:
        saudacao = "Bom dia"
    elif hora_atual < 18:
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"

    contexto = {'nome': 'Fernando', 'saudacao': saudacao}
    
    return render(request, 'core/index.html', contexto)