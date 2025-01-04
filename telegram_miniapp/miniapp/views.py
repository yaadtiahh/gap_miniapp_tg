from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
from .models import Quest


def complete_quest(request, quest_id):
    if request.method == 'POST':
        quest = Quest.objects.get(id=quest_id)
        quest.is_completed = True
        quest.save()
        return JsonResponse({'success': True, 'id': quest.id})
    return JsonResponse({'success': False}, status=400)


def get_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    return greeting


def home(request):
    greeting = get_greeting()
    return render(request, 'home.html', {"greeting": greeting})


def friends(request):
    return render(request, 'friends.html')


def profile(request):
    greeting = get_greeting()
    return render(request, 'profile.html', {"greeting": greeting})


def learn(request):
    return render(request, 'learn.html')


def quiz(request):
    return render(request, 'quiz.html')
