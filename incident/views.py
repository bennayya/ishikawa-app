"""from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Incident

def incident_list(request):
    incidents = Incident.objects.all()
    data = [{'id_incident': incident.id_incident, 'description': incident.description, 'date': incident.date.strftime('%Y-%m-%d'), 'impact': incident.impact} for incident in incidents]
    return JsonResponse({'incidents': data})

def incident_detail(request, id_incident):
    incident = get_object_or_404(Incident, id_incident=id_incident)
    data = {'id_incident': incident.id_incident, 'description': incident.description, 'date': incident.date.strftime('%Y-%m-%d'), 'impact': incident.impact}
    return JsonResponse({'incident': data})

def incident_create(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        date = request.POST.get('date')
        impact = request.POST.get('impact')
        # Assuming you handle file upload separately in Flutter and pass the file URL here
        vidmage = request.POST.get('vidmage')
        
        # Create the incident
        incident = Incident.objects.create(description=description, date=date, impact=impact, vidmage=vidmage)
        
        data = {'id_incident': incident.id_incident, 'description': incident.description, 'date': incident.date.strftime('%Y-%m-%d'), 'impact': incident.impact}
        return JsonResponse({'status': 'success', 'incident': data})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'})

def incident_update(request, id_incident):
    incident = get_object_or_404(Incident, id_incident=id_incident)
    if request.method == 'POST':
        description = request.POST.get('description')
        date = request.POST.get('date')
        impact = request.POST.get('impact')
        # Assuming you handle file upload separately in Flutter and pass the file URL here
        vidmage = request.POST.get('vidmage')
        
        # Update the incident
        incident.description = description
        incident.date = date
        incident.impact = impact
        incident.vidmage = vidmage
        incident.save()
        
        data = {'id_incident': incident.id_incident, 'description': incident.description, 'date': incident.date.strftime('%Y-%m-%d'), 'impact': incident.impact}
        return JsonResponse({'status': 'success', 'incident': data})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'})

def incident_delete(request, id_incident):
    incident = get_object_or_404(Incident, id_incident=id_incident)
    if request.method == 'POST':
        incident.delete()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'})


def show_all(request):
    incidents = Incident.objects.all()
    data = [{'id_incident': incident.id_incident, 'description': incident.description, 'date': incident.date.strftime('%Y-%m-%d'), 'impact': incident.impact} for incident in incidents]
    return JsonResponse({'incidents': data})

"""


from rest_framework import generics
from .models import Incident
from .serializers import IncidentSerializer
from django.http import JsonResponse


class IncidentList(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class IncidentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

def show_all(request):
    incidents = Incident.objects.all()
    data = [{'description': incident.description, 'impact': incident.impact, 'date': incident.date.strftime('%Y-%m-%d'), 'vidmage': incident.vidmage.url if incident.vidmage else ''} for incident in incidents]
    return JsonResponse({'incidents': data})
