from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

def HomePage(request):
	data = {
	'signup': UserCreationForm(),
	'login': AuthenticationForm(),
	}
	return render(request,'index.html',data)

def UserPage(request):
	return render(request,'user.html')

def SignUp(request):
	data = {
	'signup': UserCreationForm(),
	'login': AuthenticationForm(),
	}
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
		    form.save()
		    username = form.cleaned_data.get('username')
		    raw_password = form.cleaned_data.get('password1')
		    user = authenticate(username=username, password=raw_password)
		    login(request, user)
		    return redirect('user')
		else:
			print(form.errors)
	else:
		form = UserCreationForm()
	return render(request, 'index.html',data)

# Create your views here.
