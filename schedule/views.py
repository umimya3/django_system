from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Event, Candidate

def index(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'schedule/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event,
    }
    return render(request, 'schedule/detail.html', context)

def vote(request, event_id, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    candidate.attendance += 1
    candidate.save()
    return HttpResponseRedirect(reverse('schedule:detail', args=(event_id,)))
