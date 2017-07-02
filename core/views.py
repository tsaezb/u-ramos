from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import QuerySet
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import Ramo, Profe, Comentario, Sugerencia
from django.db.models import Avg

try:
    from django.utils import simplejson as json
except:
    import json

# Create your views here.
def Home(request):
    if request.method == "GET":
        Ramos = Ramo.objects.all()
        Profes = Profe.objects.all()
        return render(request, 'home.html', {"ramos": Ramos, "profes": Profes, "comm_status": False})
        
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
        Comentario.objects.filter(profe=profe, ramo=ramo).\
            exclude(texto__isnull=True).exclude(texto__exact=""),
    )
    return JsonResponse(comentarios, safe=False)

def save_comm(request):
    comment = request.POST.get("comm")
    new_sug = Sugerencia(texto=comment)
    new_sug.save()
    Ramos = Ramo.objects.all()
    Profes = Profe.objects.all()
    return render(request, 'home.html', {"ramos": Ramos, "profes": Profes, "comm_status": True})
    
def get_datos(request):
    def truncar(x):
        return ('%.2f' % x).rstrip('0').rstrip('.')
    
    profe = request.GET.get("id_profe")
    
    ramo = request.GET.get('nombre_ramo')
    p = Profe.objects.get(id=profe)
    r = Ramo.objects.get(name=ramo)
    PROM_importancia_asistencia_catedra = Comentario.objects.filter(profe=p, ramo= r).aggregate(Avg('importancia_asistencia_catedra'))
    PROM_importancia_asistencia_auxiliar = Comentario.objects.filter(profe=p, ramo= r).aggregate(Avg('importancia_asistencia_auxiliar'))
    PROM_exigencia_ramo_profesor = Comentario.objects.filter(profe=p, ramo= r).aggregate(Avg('exigencia_ramo_profesor'))
    comentarios = Comentario.objects.filter(profe=p, ramo= r)
    total_recomienda = comentarios.filter(recomienda=True).count()
    if comentarios.count()==0:
        porc_recom = 'No hay datos'
    else:
        porc_recom = total_recomienda*100/comentarios.count()
    return JsonResponse({"importancia_asistencia_catedra": truncar(PROM_importancia_asistencia_catedra["importancia_asistencia_catedra__avg"]),
        "importancia_asistencia_auxiliar": truncar(PROM_importancia_asistencia_auxiliar["importancia_asistencia_auxiliar__avg"]),
        "exigencia_ramo_profesor": truncar(PROM_exigencia_ramo_profesor["exigencia_ramo_profesor__avg"]),
        "recomendado": porc_recom
    })


def autocomplete(request, search_model):
    """
    Arguments:
        request
            The request object from the dispatcher
        search_model
            The search model (AKA Profe, Ramo)

    The following GET parameters can be set:
        q   The query string to filter by (match against start of string)
        p   The current page

    Response is a JSON object with following keys:
        results     List of model objects
        more        Boolean if there is more
    }
    """
    # Get model, queryset and options
    if isinstance(search_model, QuerySet):
        queryset = search_model
        search_model = queryset.model
    else:
        queryset = search_model.objects

    # Get query string
    query = request.GET.get('q', '')
    page = int(request.GET.get('p', 1))

    # Perform search
    if query:
            results = queryset.filter(name__startswith=query)
    else:
        results = queryset.all()


    # Build response
    response = {
        'results':  [model.name for model in results],
    }
    return HttpResponse(
        json.dumps(response, cls=DjangoJSONEncoder),
        content_type='application/json',
    )