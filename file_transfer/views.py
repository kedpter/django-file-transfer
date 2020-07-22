from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from file_transfer.forms import FileForm
from file_transfer.models import File
# Create your views here.

class FileCreateView(CreateView):
    template_name = 'new_file.html'
    form_class = FileForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return redirect('home')

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class FileListView(ListView):
    model = File
    template_name = 'home.html'
    context_object_name = 'files'
    ordering = '-uploaded_at'

class FileDeleteView(DeleteView):
    model = File
    success_url = reverse_lazy('home')
