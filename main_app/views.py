# from django.shortcuts import render

# # Create your views here.
# def index(request):
#     finches = [
#         {'species': 'House Finch', 'color': 'Red', 'size': 'Small'},
#         {'species': 'Goldfinch', 'color': 'Yellow', 'size': 'Small'},
#         {'species': 'Blue Jay', 'color': 'Blue', 'size': 'Medium'},
#     ]
#     return render(request, 'index.html', {'finches': finches})

# def about(request):
#     return render(request, 'about.html')
from django.shortcuts import render, get_object_or_404
from .models import Finch, Toy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    finches = Finch.objects.all()
    return render(request, 'index.html', {'finches': finches})

def about(request):
    return render(request, 'about.html')

def finch_detail(request, finch_id):
    finch = get_object_or_404(Finch, pk=finch_id)
    return render(request, 'finch_detail.html', {'finch': finch})

class FinchListView(ListView):
    model = Finch
    template_name = 'index.html'
    context_object_name = 'finches'

class FinchDetailView(DetailView):
    model = Finch
    template_name = 'finch_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedings'] = self.object.feeding_set.all()
        context['toys'] = Toy.objects.all()
        return context

class FinchCreateView(CreateView):
    model = Finch
    template_name = 'finch_form.html'
    fields = ['species', 'color', 'size']
    def get_success_url(self):
        return reverse_lazy('finch_detail', kwargs={'pk': self.object.pk})

class FinchUpdateView(UpdateView):
    model = Finch
    template_name = 'finch_form.html'
    fields = ['species', 'color', 'size']
    def get_success_url(self):
        return reverse_lazy('finch_detail', kwargs={'pk': self.object.pk})

class FinchDeleteView(DeleteView):
    model = Finch
    template_name = 'finch_confirm_delete.html'
    success_url = reverse_lazy('index')

class ToyCreateView(CreateView):
    model = Toy
    template_name = 'toy_form.html'
    fields = ['name']

    def form_valid(self, form):
        form.instance.finch_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('finch_detail', kwargs={'pk': self.kwargs['pk']})