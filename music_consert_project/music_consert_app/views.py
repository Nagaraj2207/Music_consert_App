from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from .forms import UserRegistrationForm ,UserLoginForm
from .models import Consert_list,Tickets_Booking,Booking_History
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    form = UserRegistrationForm()
    conserts = Consert_list.objects.all()
    return render(request,"home.html",{"form":form,"conserts":conserts})

def register(request):
    if request.method == 'POST':
        print(1)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(1)
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!') 
            return redirect('home')

    else:
        form = UserRegistrationForm()
    return render(request, 'music_consert.html',{"form":form})

def user_login(request):
    global user_name
    if request.method == 'POST':
        loginform = UserLoginForm(request, request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data.get('username')
            password = loginform.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                user_name = user.username
                return redirect('music_consert')
    else:
        loginform = UserLoginForm()
    return render(request, 'login.html', {"loginform": loginform})

def user_logout(request):
    logout(request)
    return redirect('home')

def music_consert(request):
    conserts = Consert_list.objects.all()
    Book_History = Booking_History.objects.filter(user_name=user_name)
    return render(request, 'music_consert.html',{"conserts":conserts,"Book_History":Book_History})


@login_required(login_url="http://127.0.0.1:8000/user_login/")
def book_tickets(request,id):
    print(id)
    current_user = User.objects.get(username=user_name)
    Consert = Consert_list.objects.get(id=id)
    print(Consert.title)
    if request.method == 'POST':
        print(1)
        ticket_count = request.POST.get('ticket')
        ticket_count = int(ticket_count)
        mydata = Tickets_Booking(title=Consert.title,ticket_count=ticket_count,user_name=current_user.username,email=current_user.email)
        mydata.save()
        book = Booking_History(title=Consert.title,venue=Consert.venue,artist=Consert.artist,ticket_count=ticket_count,user_name=current_user.username,email=current_user.email)
        book.save()
        update_count = Consert.available_tickets - ticket_count 
        Consert_list.objects.filter(id=id).update(available_tickets=update_count)
        return redirect(music_consert)
    
    return render(request, 'booktickets.html')

