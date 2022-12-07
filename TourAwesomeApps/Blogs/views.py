from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Blog
from TourAwesomeApps.Tours.models import Tour, TourImage
from .forms import createBlogForm
from django.db.models import Q
from django.contrib import messages


def createBlog(request):
    form = createBlogForm()

    if request.method == 'POST':
        form = createBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            lastBlog = Blog.objects.last() or None
            if (lastBlog is None):
                blog.id = 1
            else:
                blog.id = lastBlog.id + 1
                
            blog.save()
            
            messages.success(request, 'Tạo blog thành công!')
        
    return render(request, 'Blogs/create.html', {'form': form})


def getBlogs(request):
    blogs = Blog.objects.all() or None

    context = {
        'blogs': blogs
    }

    return render(request, 'Blogs/blogs.html', context)


def getBlog(request, pk):
    try:
        blog = Blog.objects.get(id=pk)

        relatedLocation = blog.relatedLocation
        relatedTours = Tour.objects.filter(Q(detailLocation__icontains=relatedLocation) |
            Q(location__icontains=relatedLocation))
        tours = []
        for relatedTour in relatedTours:
            image = TourImage.objects.filter(tour=relatedTour).first()
            tours.append({
                'tour': relatedTour,
                'image': image
            })
            
        content_file = open(
            'media/{0}'.format(blog.content), 'r', encoding="utf8")
        content = content_file.read()
        context = {
            'blog': blog,
            'content': content,
            'tours': tours
        }
        
        print(context)

        return render(request, 'Blogs/blog.html', context)
    except:
        blog = None
        return render(request, 'Components/404page.html')
