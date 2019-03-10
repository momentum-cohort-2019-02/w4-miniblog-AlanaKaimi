from django.shortcuts import render
from catalog.models import Blogger, BlogPost, Comment
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from .comment_form import CommentForm

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
    paginate_by = 3

class BloggerDetailView(generic.DetailView):
    model = Blogger


class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 3

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class Comment(generic.ListView):
    model = Comment

def add_comment_to_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        return redirect('blogpost-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})
