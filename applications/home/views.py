import datetime
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse

# from .models import Home, Suscriber, Contact
# from .forms import SuscribersForm, ContactForm

#from applications.entrada.models import Entry


# class FechaMixin(object):
#     def get_context_data(self, **kwargs):
#         context = super(FechaMixin, self).get_context_data(**kwargs)
#         context['fecha']= datetime.datetime.now()
#         return context

class HomePage(TemplateView):
    
    template_name = "home/index.html"
    #login_url = reverse_lazy('users_app:login')

    
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)

        #contexto de portada
        #context["home"] = Home.objects.en_home()

        #contexto para las areas de trabajo
        #context["areas_trabajo"] = Entry.objects.areas_trabajo()

        #contexto para entradas recientes
        #context["trabajos_recientes"] = Entry.objects.trabajos_recientes()

        #contexto para nosotros
        #context["nosotros"] = Entry.objects.nosotros()

        #contecto para formulario de suscripcion
        #context['form'] = SuscribersForm

        return context
