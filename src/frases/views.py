from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Frases


class FraseListView(LoginRequiredMixin, ListView):
    queryset = Frases.objects.all()
    template_name = 'Frases/listar_frase.html'
    context_object_name = 'lista_frases'


class FraseVisibleListView(ListView):
    # Cambiado: 'activo = True' por 'visible = True'
    queryset = Frases.objects.filter(visible=True)
    template_name = 'Frases/listar_frase.html'
    context_object_name = 'lista_frases'


class FraseNoVisibleListView(ListView):
    # Cambiado: 'active = False' por 'visible = False'
    queryset = Frases.objects.filter(visible=False)
    template_name = 'Frases/listar_frase.html'
    context_object_name = 'lista_frases'


class FraseCreateView(CreateView):
    model = Frases
    fields = ['autor', 'frase', 'fecha_frase']
    # Corregido: uso de paréntesis () en vez de corchetes []
    success_url = reverse_lazy('frases:listar_frase')
    template_name = 'crear.html'


class FraseUpdateView(UpdateView):
    model = Frases
    fields = '__all__'
    success_url = reverse_lazy('frases:listar_frase')
    template_name = 'crear.html'


class FraseDeleteView(DeleteView):
    model = Frases
    success_url = reverse_lazy('frases:listar_frase')
    template_name = 'frases/borrar.html'

@login_required
def detalle_frase(request, pk):
    frase = get_object_or_404(Frases, pk=pk)
    return render(request,
                  'Frases/detalle_frase.html',
                  {'frase': frase})


def modificar_activo(request, pk):
    frase_a_modificar = get_object_or_404(Frases, pk=pk)
    # Cambiado: 'activo' por 'visible'
    frase_a_modificar.visible = not frase_a_modificar.visible
    frase_a_modificar.save()
    return HttpResponseRedirect(reverse('frases:listar_frase'))


def listar_Json(request):
    frases = get_list_or_404(Frases)
    frases_json = serializers.serialize('json', frases)
    return JsonResponse(frases_json, safe=False)