from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Space
import json


def message_list(request):
    messages = Space.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'space/message_list.html', {'messages': messages})


def mark_read(request):
    id = request.GET.get('id')
    messages = Space.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    Space.objects.update_or_create(id=id, defaults={'read': True})
    return render(request, 'space/message_list.html', {'messages': messages})


def mark_all_not_read(request):
    messages = Space.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    for message in messages:
        Space.objects.update_or_create(id=message.id, defaults={'read': False})
    messages = Space.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'space/message_list.html', {'messages': messages})


def json_out_all_messages(request):
    data = []
    messages = Space.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    for message in messages:
        if not message.read:
            data.append({"id": message.id, "text": message.text})
    return HttpResponse(json.dumps(data), content_type='application/json')


def json_out_new_messages(request):
    data = []
    lastid = int(request.GET.get('last_id'))
    messages = Space.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    for message in messages:
        if (lastid < message.id) and (not message.read):
            data.append({"id": message.id, "text": message.text})
    return HttpResponse(json.dumps(data), content_type='application/json')
