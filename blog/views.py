from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Blog
from django.http import HttpResponse

# Blog page view (Displays all blogs)
def blog_list_view(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})

# Superuser blog upload page
@user_passes_test(lambda u: u.is_superuser)
def create_blog_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if not title or not content:
            return HttpResponse("Title and content are required!")
        
        # Create the blog post
        blog = Blog.objects.create(title=title, content=content, author=request.user)
        return redirect('blog_list')  # Redirect to blog list after creation
    
    return render(request, 'create_blog.html')
