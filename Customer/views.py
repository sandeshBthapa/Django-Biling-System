from django.shortcuts import render,redirect
from . forms import CustomerModelForm
from .models import Customer
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def main_page(request):
    return render(request, './../templates/index.html')


@login_required(login_url="sign_in")
def customer_create_form(request):
    if request.method == 'POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer has been created")
            return redirect('list_customer')
    
    else:
        form = CustomerModelForm()
    
    context = {
        'form': form
     }
    return render(request, 'customer_create_form.html', context)


def customer_list(request):

    fil = {}
    if request.method == "POST":
        fil["status"] = request.POST.get("status")
    enquires= Customer.objects.filter(**fil)
    context = {

        "enquires":enquires
    }
    return render(request,'list_customer.html',context)

@login_required(login_url="sign_in")
def delete_customer(request,pk):
    delete_cus = Customer.objects.get(id=pk)
    if request.method == 'POST':
        delete_cus.delete()
        messages.success(request, "Customer has been deleted")
        return redirect('list_customer')
    context = {
        'object': delete_cus
    }
    return render(request, "delete.html", context)

@login_required(login_url="sign_in")
def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerModelForm(instance=customer)
    if request.method == "POST":
        form = CustomerModelForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer has been updated")
            return redirect("list_customer")

    context = {"form": form}
    return render(request, "customer_update_form.html", context)




def signup_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Successfully Sign Up")
            return redirect("list_customer")
    else:
        form = UserCreationForm()
    context =  {"form": form}
    return render(request, "signup.html", context)

def signin_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Sign In")
                return redirect("list_customer")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "signin.html", context)

def logOutPage(request):
    logout(request)
    messages.success(request, "Successfully logOut")
    return redirect("sign_in")


