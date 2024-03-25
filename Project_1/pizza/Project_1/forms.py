from django import forms

class PizzaOrderForm(forms.Form):
    size = forms.ChoiceField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])
    crust = forms.ChoiceField(choices=[('normal', 'Normal'), ('thin', 'Thin'), ('thick', 'Thick'), ('gluten_free', 'Gluten-Free')])
    sauce = forms.ChoiceField(choices=[('tomato', 'Tomato'), ('bbq', 'BBQ')])
    cheese = forms.ChoiceField(choices=[('mozzarella', 'Mozzarella'), ('vegan', 'Vegan'), ('low_fat', 'Low Fat')])
    toppings = forms.MultipleChoiceField(choices=[
        ('pepperoni', 'Pepperoni'),
        ('chicken', 'Chicken'),
        ('ham', 'Ham'),
        ('pineapple', 'Pineapple'),
        ('peppers', 'Peppers'),
        ('mushrooms', 'Mushrooms'),
        ('onions', 'Onions'),
    ], widget=forms.CheckboxSelectMultiple)
