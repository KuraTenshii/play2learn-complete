from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GameHistory(models.Model):
    GAME_CHOICES = [
        ("math_facts", "Math Facts Practice"),
        ("anagram_hunt", "Anagram Hunt"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="game_histories")
    game_type = models.CharField(max_length=20, choices=GAME_CHOICES)
    settings = models.JSONField()  # store game-specific settings as JSON
    final_score = models.IntegerField()
    finished_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-finished_at"]

    def __str__(self):
        return f"{self.user.username} - {self.get_game_type_display()} - {self.final_score}"
