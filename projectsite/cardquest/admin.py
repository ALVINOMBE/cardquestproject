from django.contrib import admin
from .models import PokemonCard, Trainer, Collection
# Register your models here.

@admin.register(PokemonCard)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity")
    search_fields = ("name",)

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name","birthdate","location","email")
    search_fields = ("name",)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("card", "trainer", "collection_date")
    search_fields = ("card", "trainer")