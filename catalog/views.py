from django.shortcuts import render
from catalog.models import Blogger, BlogPost
from django.views import generic
from django.urls import reverse, reverse_lazy

# Create your views here.

def index(request):
    """View function for home page of site"""

    # Generates counts of some of the main objects
    num_bloggers = Blogger.objects.all().count()
    num_posts = BlogPost.objects.all().count()

    context = {
        'num_bloggers': num_bloggers,
        'num_posts': num_posts,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger


class BlogPostListView(generic.ListView):
    model = BlogPost

class BlogPostDetailView(generic.DetailView):
    model = BlogPost