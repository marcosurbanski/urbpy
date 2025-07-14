from django.shortcuts import render

from pypro.modulos import facade


def indice(request):
    return render(request, 'modulos/indice.html')


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})


def aula(request, slug):
    aula = facade.encontrar_aula(slug)
    modulo = aula.modulo
    aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)

    index = aulas.index(aula)
    aula_anterior = aulas[index - 1] if index > 0 else None
    aula_proxima = aulas[index + 1] if index < len(aulas) - 1 else None

    context = {
        'aula': aula,
        'modulo': modulo,
        'aula_anterior': aula_anterior,
        'aula_proxima': aula_proxima,
    }

    return render(request, 'modulos/aula_detalhe.html', context)
