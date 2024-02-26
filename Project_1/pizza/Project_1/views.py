from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import PizzaSize, PizzaCrust, PizzaSauce, CheeseType, PizzaTopping, Pizza, Order

def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('order_history') 
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('order_history')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html', {'orders': orders})


@login_required
def create_pizza(request):
    if request.method == 'POST':

        size_name = request.POST.get('size')
        crust_name = request.POST.get('crust')
        sauce_name = request.POST.get('sauce')
        cheese_name = request.POST.get('cheese')
        topping1 = request.POST.get('topping1')
        topping2 = request.POST.get('topping2')
        topping3 = request.POST.get('topping3')
        topping4 = request.POST.get('topping4')
        topping5 = request.POST.get('topping5')
        topping6 = request.POST.get('topping6')
        topping7 = request.POST.get('topping7') 

        size = get_object_or_404(PizzaSize, name=size_name)
        crust = get_object_or_404(PizzaCrust, name=crust_name)
        sauce = get_object_or_404(PizzaSauce, name=sauce_name)
        cheese = get_object_or_404(CheeseType, name=cheese_name)

        
        pizza = Pizza.objects.create(
            size=size,
            crust=crust,
            sauce=sauce,
            cheese=cheese
        )
        
        if topping1:
            topping, created = PizzaTopping.objects.get_or_create(name='pepperoni')
            pizza.toppings.add(topping)
        if topping2:
            topping, created = PizzaTopping.objects.get_or_create(name='chicken')
            pizza.toppings.add(topping)
        if topping3:
            topping, created = PizzaTopping.objects.get_or_create(name='ham')
            pizza.toppings.add(topping)
        if topping4:
            topping, created = PizzaTopping.objects.get_or_create(name='pineapple')
            pizza.toppings.add(topping)
        if topping5:
            topping, created = PizzaTopping.objects.get_or_create(name='peppers')
            pizza.toppings.add(topping)
        if topping6:
            topping, created = PizzaTopping.objects.get_or_create(name='mushrooms')
            pizza.toppings.add(topping)
        if topping7:
            topping, created = PizzaTopping.objects.get_or_create(name='onions')
            pizza.toppings.add(topping)

        request.session['pizza_id'] = pizza.id

        return redirect('delivery_details')
    else:
        return render(request, 'create_pizza.html')


@login_required
def delivery_details(request):
    if request.method == 'POST':
      


        request.session['delivery_details'] = {
            'delivery_address': request.POST.get('delivery_address'),
            'delivery_date_time': request.POST.get('delivery_date_time'),
            'payment_info': request.POST.get('payment_info'),
        }

        return redirect('order_summary')  

    return render(request, 'delivery_details.html')

@login_required
def order_summary(request):

    pizza_id = request.session.get('pizza_id')
    delivery_details = request.session.get('delivery_details')

    if not pizza_id or not delivery_details:
        return redirect('create_pizza')  
   
    pizza = get_object_or_404(Pizza, pk=pizza_id)

    context = {
        'delivery_address': delivery_details['delivery_address'],
        'delivery_date_time': delivery_details['delivery_date_time'],
        'payment_info': delivery_details['payment_info'],
        'pizza': pizza,
        'toppings': pizza.toppings.all(),
    }

    return render(request, 'order_summary.html', context)