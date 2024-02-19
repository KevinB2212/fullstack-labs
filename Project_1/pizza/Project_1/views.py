from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login

from .models import PizzaSize, PizzaCrust, PizzaSauce, CheeseType, PizzaTopping, Pizza


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

            return redirect('order_history.html')  # Redirect to order history after registration

    else:

        form = UserCreationForm()

    return render(request, 'order_history.html', {'form': form})


def login_view(request):

    if request.method == 'POST':

        return redirect('order_history')

    else:

        # Render login form

        return render(request, 'login.html')


from .models import Order


def order_history(request):

    orders = Order.objects.filter(user=request.user)

    return render(request, 'order_history.html', {'orders': orders})


from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login

from .models import PizzaSize, PizzaCrust, PizzaSauce, CheeseType, PizzaTopping, Pizza

def jls_extract_def():
    return Pizza.objects


def create_pizza(request):

    if request.method == 'POST':

        # Process the form data

        size_name = request.POST.get('size')

        crust = request.POST.get('crust')

        sauce = request.POST.get('sauce')

        cheese = request.POST.get('cheese')

        toppings = request.POST.getlist('toppings')


        # Get the PizzaSize instance corresponding to the selected size

        size = get_object_or_404(PizzaSize, name=size_name)


        # Create a new Pizza instance

        pizza = jls_extract_def().create(
            size=size,
            crust=crust,
            sauce=sauce,
            cheese=cheese
        )
        pizza.toppings.add(*toppings)

        # Redirect to delivery details page
        return redirect('delivery_details.html')  # Redirect to delivery_details.html
    else:
        return render(request, 'create_pizza.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from .models import PizzaSize, PizzaCrust, PizzaSauce, CheeseType, PizzaTopping, Pizza


def delivery_details(request):

    if request.method == 'POST':

        # Process form data and save to database if needed

        return redirect('order_summary')  # Redirect to order summary page after filling delivery details

    return render(request, 'delivery_details.html')


def order_summary(request):

    # Retrieve order details and render order summary page

    return render(request, 'order_summary.html')

