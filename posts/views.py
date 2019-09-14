from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Update

class UpdateView(ListView):
	model = Update
	template_name = 'index.html'
	context_object_name = 'comments'

class DetailPostView(DetailView):
	model = Update
	template_name = 'detailed.html'

