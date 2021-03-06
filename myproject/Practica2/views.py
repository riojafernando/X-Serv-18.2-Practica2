from django.shortcuts import render
from models import ACORTADOR
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def formulario(request):
    salida = ''
    url = '' 
    formulario = '<form action="" method="POST">'
    formulario += 'Put here your URL: <input type="text" name="valor">'
    formulario += '<input type="submit" value="Send">'
    formulario += '</form>'
    lista = ACORTADOR.objects.all()

    if request.method == 'POST':
        if request.POST['valor'].find('http') == -1:
            url = 'http://' + request.POST['valor']
        else:
            url = request.POST['valor']

        for fila in lista:
            if fila.url == url:
                return HttpResponse('This url ' + url + ' is already short with ID = ' + str(fila.id))

        database = ACORTADOR(url=url)
        database.save()

    lista = ACORTADOR.objects.all()
    salida = '<h1>' + 'We have these URLs:' '</h1>' + '<br>'
    for fila in lista:
        salida += '<li>' + fila.url + ', ID = ' + str(fila.id)
    return HttpResponse(formulario + '<br>' + salida)

def Busqueda(request, recurso):
    try:
        database = ACORTADOR.objects.get(id=recurso)
        return HttpResponseRedirect(database.url)
    except ACORTADOR.DoesNotExist:
        return HttpResponse('Resource /' + recurso + ' not found')
