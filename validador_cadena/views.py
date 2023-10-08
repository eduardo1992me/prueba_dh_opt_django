from django.shortcuts import render
from django.http import HttpResponse
from validador_cadena.decryptor import reader


# Create your views here.
def main_view(request):
    if request.method == 'POST':
        cadena = request.POST.get('cadena')
        resultado = reader(cadena)
        return render(request, 'main.html', {'resultado' :resultado})
    return render(request, 'main.html')