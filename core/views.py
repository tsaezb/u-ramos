from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import Ramo, Profe, Comentario
try:
    from django.utils import simplejson as json
except:
    import simplejson as json

# Create your views here.
def Home(request):
    if request.method == "GET":
        Ramos = Ramo.objects.all()
        Profes = Profe.objects.all()
        return render(request, 'home.html', {"ramos": Ramos, "profes": Profes})
        
def getdetails(request):
    ramo_name = request.POST['rmo']
    print "ajax ramo_name ", ramo_name

    result_set = []
    all_profs = []
    selected_ramo = Ramo.objects.get(name=ramo_name)
    #print "ramo seleccionado", selected_ramo
    all_profs = selected_ramo.profe_set.all()
    for profe in all_profs:
        result_set.append({
            'name': profe.name,
            'id': profe.id
        })
    return JsonResponse(result_set, safe=False)
    
def comentarios_ajax(request):
    nombre_ramo = request.GET.get('nombre_ramo')
    ramo = Ramo.objects.get(name=nombre_ramo)
    id_profe = request.GET.get('id_profe')
    profe = Profe.objects.get(id=id_profe)
    comentarios = serializers.serialize('json',
        Comentario.objects.filter(profe=profe, ramo=ramo),
    )
    return JsonResponse(comentarios, safe=False)
