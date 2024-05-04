from django.shortcuts import render;
from django.http import HttpResponse;
from instruments.models import keyboard, drum, guitar, violin, feedback;
from login.models import users;
from instruments.forms import keyboardForm, drumForm, guitarForm, violinForm, feedbackForm;
from instruments.models import orders;



# Create your views here.
def index(request):
    # Check if its a POST request
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['username']
        loginpassword = request.POST['psw']
        # Check if user has entered correct credentials
        user = users.objects.filter(username=loginusername, password=loginpassword)
        if user:
            request.session['username'] = loginusername
            return render(request, 'Website.html', {'username': loginusername})
        else:
            return render(request, 'login.html', {'error': 'Please enter valid credentials'})
    else:
        username = request.session.get('username')
        if username:
            return render(request, 'Website.html', {'username': username})
        else:
            return render(request, 'login.html', {'error': 'Please login first'})

def about(request):
    username = request.session.get('username')
    if username:
        return render(request, 'aboutus.html', {'username': username})
    else:
        return render(request, 'login.html', {'error': 'Please login first'})

def contact(request):
    username = request.session.get('username')
    if username:
        return render(request, 'contact.html', {'username': username})
    else:
        return render(request, 'login.html', {'error': 'Please login first'})

def careers(request):
    username = request.session.get('username')
    if username:
        return render(request, 'career.html', {'username': username})
    else:
        return render(request, 'login.html', {'error': 'Please login first'})

def signup(request):
    # Check if its a POST request
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        password = request.POST['psw']
        # Check if password is 4 letters long
        if len(password) < 4:
            return render(request, 'signup.html', {'error': 'Password must be atleast 4 characters long'})
        # Check if username follows the regex
        if not username.isalnum():
            return render(request, 'signup.html', {'error': 'Username must contain only alphanumeric characters'})
        # Check if user has entered correct credentials
        user = users.objects.filter(username=username)
        if user:
            return render(request, 'signup.html', {'error': 'Username already exists'})
        else:
            user = users(username=username, password=password)
            user.save()
            return render(request, 'login.html', {'error': 'Account created successfully'})
    else:
        username = request.session.get('username')
        if username:
            return render(request, 'Website.html', {'username': username})
        else:
            return render(request, 'signup.html')

def instruments(request):
    username = request.session.get('username')
    if username:
        return render(request, 'instrument.html', {'username': username})
    else:
        return render(request, 'login.html', {'error': 'Please login first'})

def products(request):
    username = request.session.get('username')
    if username:
        item = request.GET['item']
        if item == 'keyboard':
            queryset = keyboard.objects.all()
        elif item == 'drum':
            queryset = drum.objects.all()
        elif item == 'guitar':
            queryset = guitar.objects.all()
        elif item == 'violin':
            queryset = violin.objects.all()
        else:
            return render(request, 'instrument.html', {'error': 'Please select a valid instrument and try again'})
        data = list(queryset.values())
        return render(request, 'product.html', {'username': username, 'data': data, 'item': item})
    else:
        return render(request, 'login.html', {'error': 'Please login first'})

def login(request):
    username = request.session.get('username')
    if username:
        return render(request, 'Website.html', {'username': username})
    else:
        return render(request, 'login.html')

def buy(request):
    username = request.session.get('username')
    if username:
        if request.method == "GET":
            item = request.GET['item']
            id = request.GET['id']
            if item == 'keyboard':
                queryset = keyboard.objects.filter(id=id)
            elif item == 'drum':
                queryset = drum.objects.filter(id=id)
            elif item == 'guitar':
                queryset = guitar.objects.filter(id=id)
            elif item == 'violin':
                queryset = violin.objects.filter(id=id)
            else:
                return render(request, 'instrument.html', {'error': 'Please select a valid instrument and try again'})
            if queryset:
                data = list(queryset.values())
                return render(request, 'buy.html', {'username': username, 'product': data[0], 'item': item})
            else:
                return render(request, 'instrument.html', {'error': 'Please select a valid instrument and try again'})
        else:
            name = request.session.get('username')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            item = request.POST.get('item')
            id = request.POST.get('id')
            order = orders(name=name, address=address, phone=phone, item=item, id=id)
            order.save()
            msg = "Your order has been placed successfully"
            return render(request, 'buy.html', {'username': username, 'msg': msg})
    else:
        return render(request, 'login.html', {'error': 'Please login first'})

def features(request):
    username = request.session.get('username')
    if username:
        return render(request, 'features.html', {'username': username})
    else:
        return render(request, 'login.html', {'error': 'Please login first'})
    
def logout(request):
    request.session.clear()
    return render(request, 'login.html', {'error': 'Logged out successfully'})

def add_instrument(request):
    username = request.session.get('username')
    if username:
        return render(request, 'add_instrument.html', {'username': username})
    else:
        return render(request, 'login.html', {'error': 'Please login first'})
    
def add_form(request):
    if request.method == 'GET':
        form_type = request.GET['form_type']
        if form_type == 'keyboard':
            form = keyboardForm()
        elif form_type == 'drum':
            form = drumForm()
        elif form_type == 'guitar':
            form = guitarForm()
        elif form_type == 'violin':
            form = violinForm()
        else:
            return render(request, 'add_instrument.html', {'error': 'Please select a valid instrument and try again'})
        return render(request, 'add_form.html', {'form': form, 'form_type': form_type})
    elif request.method == "POST":
        item = request.POST.get('item')
        if item == "keyboard":
            form = keyboardForm(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                price = form.cleaned_data['price']
                description = form.cleaned_data['description']
                image = form.cleaned_data['image']
                keyboard_obj = keyboard(name=name, price=price, description=description, image=image)
                keyboard_obj.save()
                return render(request, 'add_instrument.html', {'error': 'Instrument added successfully'})
            else:
                return render(request, 'add_form.html', {'error': 'Please enter valid details and try again', 'form_type': 'keyboard'})
        elif item == "drum":
            form = drumForm(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                price = form.cleaned_data['price']
                description = form.cleaned_data['description']
                image = form.cleaned_data['image']
                drum_obj = drum(name=name, price=price, description=description, image=image)
                drum_obj.save()
                return render(request, 'add_instrument.html', {'error': 'Instrument added successfully'})
            else:
                return render(request, 'add_form.html', {'error': 'Please enter valid details and try again', 'form_type': 'drum'})
        elif item == "guitar":
            form = guitarForm(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                price = form.cleaned_data['price']
                description = form.cleaned_data['description']
                image = form.cleaned_data['image']
                guitar_obj = guitar(name=name, price=price, description=description, image=image)
                guitar_obj.save()
                return render(request, 'add_instrument.html', {'error': 'Instrument added successfully'})
            else:
                return render(request, 'add_form.html', {'error': 'Please enter valid details and try again', 'form_type': 'guitar'})
        elif item == "violin":
            form = violinForm(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                price = form.cleaned_data['price']
                description = form.cleaned_data['description']
                image = form.cleaned_data['image']
                violin_obj = violin(name=name, price=price, description=description, image=image)
                violin_obj.save()
                return render(request, 'add_instrument.html', {'error': 'Instrument added successfully'})
            else:
                return render(request, 'add_form.html', {'error': 'Please enter valid details and try again', 'form_type': 'violin'})
        else:
            return render(request, 'add_instrument.html', {'error': 'Please select a valid instrument and try again'})
        
def remove_form(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        id = request.POST.get('id')
        if item == "keyboard":
            queryset = keyboard.objects.filter(id=id)
        elif item == "drum":
            queryset = drum.objects.filter(id=id)
        elif item == "guitar":
            queryset = guitar.objects.filter(id=id)
        elif item == "violin":
            queryset = violin.objects.filter(id=id)
        else:
            return render(request, 'remove_form.html', {'error': 'Please select a valid instrument and try again'})
        if queryset:
            queryset.delete()
            return render(request, 'remove_form.html', {'error': 'Instrument removed successfully'})
        else:
            return render(request, 'remove_form.html', {'error': 'Please select a valid item and try again'})
    else:
        return render(request, 'remove_form.html')

def fb(request):
    form = feedbackForm()
    if request.method == "GET":
        return render(request, 'feedback.html', {'form': form})
    else:
        form = feedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            msg = form.cleaned_data['feedback']
            rating = form.cleaned_data['rating']
            fedback_obj = feedback(name=name, feedback=msg, rating=rating)
            fedback_obj.save()
            return render(request, 'feedback.html', {'error': 'Your feedback was submitted successfully', 'form': form})
        else:
            return render(request, 'feedback.html', {'error': 'Invalid data entered!', 'form': form})

