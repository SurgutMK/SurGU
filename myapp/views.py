from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView
from myapp.models import Person

# Create your views here.
# def index(request):
#     return HttpResponse('hello')

def index(request):
    context = {'names': ['Tom', 'John', 'Alex'], 
                'div': '<div>wefsfsdfsdf</div>'}
    return render(request, 'myapp/index.html', context)

class CustomTemplateView(TemplateView):
    template_name = 'myapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["names"] = ['Tom', 'John', 'Alex']
        return context

class CustomListView(ListView):
    model = Person
    
    