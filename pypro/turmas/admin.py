from django.contrib import admin

# Register your models here.
from pypro.turmas.models import Turma


class MatriculaInline(admin.TabularInline):
    model = Turma.alunos.through


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inLines = [MatriculaInline]
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)
