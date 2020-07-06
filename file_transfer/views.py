from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from django.views.generic import TemplateView

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

class FileListView(ListView):
    model = File
    template_name = 'home.html'
    context_object_name = 'files'

class FileDeleteView(DeleteView):
    model = File
    success_url = reverse_lazy('home')
