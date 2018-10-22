from django.db import models
from django.contrib import admin


class Player(models.Model):
    player_name = models.CharField(max_length=100)
    world_ranking = models.IntegerField()
    age = models.IntegerField()
    years_pro = models.IntegerField()

    def __str__(self):
        return self.player_name


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass
