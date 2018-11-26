from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import OrderForm
from .forms import OrderModelForm
from .forms import ProductModelForm
from .models import ProductForm


def index(request):
    latest_order_list = OrderForm.objects.order_by('-current_date')[:5]
    print(latest_order_list)
    context = {'latest_order_list': latest_order_list}
    return render(request, 'polls/index.html', context)


def detail(request, order_id):
    order = get_object_or_404(OrderForm, pk=order_id)
    return render(request, 'polls/detail.html', {'order': order,"order_id":order_id})


def results(request, order_id):
    response = "You're looking at the results of the order %s."
    return HttpResponse(response % order_id)


def input(request):
    #print(request.method)
    if request.method == "POST":
        #print(request.POST)

        form = OrderModelForm(request.POST)

        if form.is_valid():
            model_instance = form.save(commit=True)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect('/')
    else:
        form = OrderModelForm()

        return render(request, 'polls/inputPage.html', {'form': form})

    return render(request, 'polls/inputPage.html')

def productinput(request):
    #print(request.method)
    if request.method == "POST":
        #print(request.POST)
        form = ProductModelForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=True)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect('/polls/query/')
    else:
        form = ProductModelForm()
        return render(request, 'polls/productInput.html', {'form': form})

    return render(request, 'polls/productInput.html')
def  query(request):
    try:
        product=ProductForm.objects.get(product_id=request.POST["id"])
        print(product)
        context={'product':product}
        return render(request, 'polls/displayProduct.html', context)
    except:
        return render(request,'polls/query.html')

def vote(request, order_id):
    return HttpResponse("You're voting on question %s." % order_id)