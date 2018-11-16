from django.db import models
from django.contrib import admin
from djongo import models as mongo_model


class Player(models.Model):
    player_name = models.CharField(max_length=100)
    world_ranking = models.IntegerField()
    age = models.IntegerField()
    years_pro = models.IntegerField()

    def __str__(self):
        return self.player_name


class PlayerBio(mongo_model.Model):
    player_name = mongo_model.CharField(max_length=100)
    world_ranking = mongo_model.IntegerField()
    age = mongo_model.IntegerField()
    years_pro = mongo_model.IntegerField()

    def __str__(self):
        return self.player_name


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass


@admin.register(PlayerBio)
class PlayerBioAdmin(admin.ModelAdmin):
    pass
