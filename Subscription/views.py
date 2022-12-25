from django.shortcuts import render,redirect, HttpResponse
from .models import Subscription
from django.contrib import messages
from .forms import SubscriptionCreateForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def all_subscription(request):
    fil = {}
    if request.method == "POST":
        fil["status"] = request.POST.get("status")
    enquires= Subscription.objects.filter(**fil)
    context = {

        "enquires":enquires
    }
    return render(request, 'all_subscription.html',context)


@login_required(login_url="sign_in")
def create_subscription(request):
    form = SubscriptionCreateForm
    if request.method == 'POST':
        if request.user.groups.filter(permissions__name='Can add subscription'):
            form = SubscriptionCreateForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "subscription has been created")
                return redirect('all_sub')
        else:
            return HttpResponse('Permission not granted')

    context = {
        'form': form
     }
    
    return render(request, 'subscription_create_form.html', context)


@login_required(login_url="sign_in")
def delete_subscription(request,pk):
    delete_sub = Subscription.objects.get(id=pk)
    if request.method == 'POST':
        if request.user.groups.filter(permissions__name='Can delete subscription'):
            delete_sub.delete()
            messages.success(request, "subscription has been deleted")
            return redirect('all_sub')
        else:
            return HttpResponse('Permission not granted')
    context = {
        'object': delete_sub
    }
    return render(request, "delete_subscription.html", context)


@login_required(login_url="sign_in")

def update_subscription(request, pk):
    customer = Subscription.objects.get(id=pk)
    form = SubscriptionCreateForm(instance=customer)
    if request.method == "POST":
        if request.user.groups.filter(permissions__name='Can change subscription'):
            form = SubscriptionCreateForm(request.POST, instance=customer)
            if form.is_valid():
                form.save()
                messages.success(request, "subscription has been updated")
                return redirect("all_sub")
        else:
            return HttpResponse('Permisssion not granted')

    context = {"form": form}
    return render(request, "update_subscription.html", context)




  