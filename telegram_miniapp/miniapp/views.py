from django.http import JsonResponse
from django.shortcuts import render
from .models import Quest


def complete_quest(request, quest_id):
    if request.method == 'POST':
        quest = Quest.objects.get(id=quest_id)
        quest.is_completed = True
        quest.save()
        return JsonResponse({'success': True, 'id': quest.id})
    return JsonResponse({'success': False}, status=400)


def home(request):
    return render(request, 'home.html')


def friends(request):
    return render(request, 'friends.html')


def profile(request):
    return render(request, 'profile.html')


def learn(request):
    return render(request, 'learn.html')


def quiz(request):
    return render(request, 'quiz.html')
