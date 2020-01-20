from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.http import HttpResponse

# Create your views here.

class EntryList(ListView):
	template_name = 'base.html'
	model = Post


	def get(self, request):
		print('Hawkguy!')
		posts = Post.objects.all()
		print(posts)
		return HttpResponse(posts)
		

class EntryDetail(DetailView):
	template_name = 'detail.html'
	
	queryset = Post.objects.all()


class BookCreateView(CreateView):
    template_name = 'create_view.html'
    model = Post
    fields = ['Title', 'Body', 'Author']

class BookUpdateView(UpdateView):
    template_name = 'update_view.html'
    model = Post
    fields = ['Title', 'Body', 'Author']

class BookDeleteView(DeleteView):
    template_name = 'delete_view.html'
    model = Post
    success_url = reverse_lazy('home')