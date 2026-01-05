from django.contrib import admin
from .models import GameHistory
# Register your models here.

@admin.register(GameHistory)
class GameHistoryAdmin(admin.ModelAdmin):
    list_display = ("user", "game_type", "final_score", "finished_at")
    list_filter = ("game_type",)
    ordering = ("-finished_at",)