from django.contrib import admin
from .models import Quest  # Импортируем модель Quest


@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed')  # Какие поля отображать в списке
    list_filter = ('is_completed',)          # Фильтр по статусу выполнения
    search_fields = ('title',)
