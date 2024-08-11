from django.shortcuts import render, redirect
from vege.models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


# here we have protected the route using this decorator
@login_required(login_url='/login/')
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        # This is how you grab files from frontend
        receipe_image = request.FILES.get('receipe_image')

        print("Receipe Name: ", receipe_name)
        print("Receipe Description: ", receipe_description)
        print("Receipe Image: ", receipe_image)

        Receipe.objects.create(
            receipe_name=receipe_name, receipe_description=receipe_description, receipe_Image=receipe_image)

        return redirect('/receipes/')

    queryset = Receipe.objects.all()
    # handling search functionality:
    if request.GET.get('search'):
        # This is how you grab the value of search value using GET method
        print(request.GET.get('search'))
        filtered_receipes = queryset.filter(
            receipe_name__icontains=request.GET.get('search'))
        queryset = filtered_receipes

    context = {
        'receipes': queryset
    }

    return render(request, 'receipes.html', context)


@login_required(login_url='/login/')
def update_receipe(request, id):
    # grabbing data from the database to display
    selected_receipe = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        # grabbing all fields daya coming from front end
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        # updating them:
        selected_receipe.receipe_name = receipe_name
        selected_receipe.receipe_description = receipe_description
        if receipe_image:
            selected_receipe.receipe_Image = receipe_image
        # finally saving the updated data in database
        selected_receipe.save()
        return redirect('/receipes/')

    context = {'receipe': selected_receipe}

    return render(request, 'update_receipe.html', context)


@login_required(login_url='/login/')
def delete_receipe(request, id):
    print("ID: ", id)

    selected_receipe = Receipe.objects.get(id=id)
    selected_receipe.delete()
    return redirect('/receipes/')


def register_page(request):

    if request.method == "POST":
        # grabbing the data coming from front end
        data = request.POST
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')

        # checking the user already exists (handling error)
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(
                request, "Username already taken. Choose a unique one!")
            return redirect('/register/')

        # adding data inside User model. here user is coming from models.py
        user = User.objects.create(
            first_name=first_name, last_name=last_name, username=username)
        user.set_password(password)  # for hashing the password

        # saving the data
        user.save()
        messages.info(request, "User created successfully")

        return redirect('/login/')  # fixed typo here

    return render(request, 'register_page.html')


def login_page(request):
    if request.method == "POST":
        # grabbing the data coming from front end
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        # checking if the user exists with this username or not

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')

            # using django builtin method for credentials verification
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # using django builtin login method for creating the session for the user
            login(request, user)
            return redirect('/receipes/')

    return render(request, 'login_page.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')
