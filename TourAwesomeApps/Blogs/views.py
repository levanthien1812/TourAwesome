from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Blog
from .forms import createBlogForm

def getBlogs(request):
    blogs = Blog.objects.all() or None
    
    return blogs

def createBlog(request):
    form = createBlogForm()
    
    if request.method == 'POST':
        form = createBlogForm(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request, 'Blogs/create.html', {'form': form})

def getBlog(request, pk):
    blog = Blog.objects.filter(id=pk).get() or None
    
    if (blog == None):
        raise Http404('Không tìm thấy blog này')
    
    context = {
        'blog': blog
    }
    
    return render(request, 'Blogs/blog.html', context)
    