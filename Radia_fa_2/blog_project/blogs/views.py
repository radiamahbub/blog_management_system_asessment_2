from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth. decorators import login_required
from django.shortcuts import get_object_or_404
from blogs. models import *
from django.contrib import messages
from blogs.forms import *

# Create your views here.

def home(request):
    return render(request, 'blogs/home.html')

# --------------CRUD----------------------
def blog_add(request):
    
    form_data = BlogForm()
    if request.method == 'POST':
         form_data = BlogForm(request.POST, request.FILES)
         if form_data.is_valid():
              form_data.save()
              return redirect('blog_list')
    context = {
         'form_data': form_data
    }

    return render(request, 'blogs/blog_add.html', context)

    # if request.method == "POST":
        #         title = request.POST.get('title')
        #         author_name = request.POST.get('author_name')
        #         content = request.POST.get('content')
        #         catagory = request.POST.get('catagory')
        #         blog_image = request.FILES.get('blog_image')
    
        #         BlogModel.objects.create(
        #             title=title,
        #             author_name=author_name,
        #             content=content,
        #             catagory=catagory,
        #             blog_image=blog_image
        #         )
        #         return redirect('blog_list')
        # return render(request, 'blogs/blog_add.html', context)

def blog_list(request):

    b_data = BlogModel.objects.all()

    context = {
        'b_data':b_data
    }

    return render(request, 'blogs/blog_list.html', context)

def blog_update(request, b_id):
    
    b_data = get_object_or_404(BlogModel, id=b_id)
    print(b_data)
    form_data = BlogForm(instance=b_data)

    if request.method == 'POST':
             form_data = BlogForm(request.POST, request.FILES, instance=b_data)
             if form_data.is_valid():
                  form_data.save()
                  return redirect('blog_list')

    context = {
             'form_data': form_data
        }
    
    return render(request, 'blogs/blog_update.html', context)
    


    # b_data = BlogModel.objects.get(id=b_id)

    # if request.method == "POST":
    #         title = request.POST.get('title')
    #         author_name = request.POST.get('author_name')
    #         content = request.POST.get('content')
    #         catagory = request.POST.get('catagory')
    #         blog_image = request.FILES.get('blog_image')

    #         b_data.title =title
    #         b_data.author_name  =author_name

    #         if blog_image:
    #             b_data.blog_image =blog_image

    #         b_data.content=content
    #         b_data.catagory =catagory

    #         b_data.save()

    #         return redirect('blog_list')

    # context = {
    #     'b_data':b_data
    # }

    # return render(request, 'blog/update_blog.html', context)


def blog_delete(request, b_id):
    b_data = get_object_or_404(BlogModel, id=b_id)
    b_data.delete()
    return redirect('blog_list')



#------------------Authentication---------------------

def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')

        user_exits = UserModel.objects.filter(username=username).exists()
        if user_exits:
             messages.warning(request, 'User already exits!')
             return redirect('register')
        

        if password == c_password:
            UserModel.objects.create_user(
                username=username,
                full_name=full_name,
                email=email,
                password=password,
            )
            return redirect('login')

         
    return render(request, 'blogs/register_page.html')

def login_page(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_info = authenticate(request, username=username, password=password)
            if user_info:
                login(request, user_info)
                return redirect('home')
            else:
                messages.warning(request, 'Invalid Credentils!!!')


    return render(request, 'blogs/login_page.html')

def logout_page(request):
    logout(request)
    return redirect('login')

