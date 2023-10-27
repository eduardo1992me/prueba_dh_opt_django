from django.shortcuts import render
from django.http import HttpResponse
from validador_cadena.decryptor import reader_pro


# Create your views here.
def main_view(request):
    if request.method == 'POST':
        cadena = request.POST.get('cadena')
        resultado = reader_pro(cadena)
        print(resultado["result"])
        if resultado["result"] == True:
            return render(request, 'main.html', {'resultado' :resultado})
        else:
            return render(request, 'main.html', {'resultado_error' :resultado})
    return render(request, 'main.html')