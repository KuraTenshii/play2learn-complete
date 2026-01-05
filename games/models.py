from django.db import models
from django.contrib.auth.models import User


class GameHistory(models.Model):
    GAME_CHOICES = [
        ("math_facts", "Math Facts"),
        ("anagram_hunt", "Anagram Hunt"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="game_histories"
    )

    game_type = models.CharField(
        max_length=20,
        choices=GAME_CHOICES
    )

    final_score = models.IntegerField()

    settings = models.JSONField(
        blank=True,
        default=dict
    )

    finished_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-finished_at"]

    def __str__(self):
        return f"{self.user.username} | {self.game_type} | {self.final_score}"
