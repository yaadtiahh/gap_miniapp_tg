from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def invite(request):
    return render(request, 'invite.html')


def profile(request):
    return render(request, 'profile.html')


def learn(request):
    return render(request, 'learn.html')


def quiz(request):
    return render(request, 'quiz.html')