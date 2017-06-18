from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Ramo, Profe
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
        #print "profe name", profe.name
        result_set.append({'name': profe.name})
    return JsonResponse(result_set, safe=False)