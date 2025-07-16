from django.shortcuts import render 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Page
from django.contrib.auth.mixins import LoginRequiredMixin

class PageListView(ListView):
    model = Page
    template_name = 'paginas/page_list.html'
    context_object_name = 'pages'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get
        if query:
            queryset = queryset.filter(titulo__icontains=query)
            return queryset
            
class PageDetailView(DetailView):
    model = Page
    template_name = 'paginas/page_detail.html'
    context_object_name = 'page'

class PageCreateView(CreateView):
    model = Page
    template_name = 'paginas/page_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('page_list')

class PageUpdateView(UpdateView):
    model = Page
    template_name = 'paginas/page_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('page_list')

class PageDeleteView(DeleteView):
    model = Page
    template_name = 'paginas/page_confirm_delete.html'
    success_url = reverse_lazy('page_list')

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    template_name = 'paginas/page_form.html'
    success_url = reverse_lazy('page_list')