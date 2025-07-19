from django.shortcuts import render, redirect
from .models import Order

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        cart = {
            'espresso': int(request.POST.get('espresso', 0)),
            'latte': int(request.POST.get('latte', 0)),
            'cappuccino': int(request.POST.get('cappuccino', 0)),
            'brownie': int(request.POST.get('brownie', 0)),
            'croissant': int(request.POST.get('croissant', 0)),
            'iced_mocha': int(request.POST.get('iced_mocha', 0)),
        }

        total = (
            cart['espresso'] * 90 +
            cart['latte'] * 120 +
            cart['cappuccino'] * 110 +
            cart['brownie'] * 70 +
            cart['croissant'] * 80 +
            cart['iced_mocha'] * 130
        )

        request.session['cart'] = cart
        request.session['total'] = total
        request.session['name'] = name
        request.session['email'] = email
        request.session['message'] = message

        return redirect('address')

    return render(request, 'cafe/home.html')


def address(request):
    if request.method == 'POST':
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        phone = request.POST.get('phone')

        full_address = f"{street}, {city}, {state} - {zip_code}\nPhone: {phone}"
        request.session['address'] = full_address  # ✅ Save to session

        return redirect('payment')

    return render(request, 'cafe/address.html')


def payment(request):
    cart = request.session.get('cart', {})
    total = request.session.get('total', 0)
    name = request.session.get('name', '')
    email = request.session.get('email', '')
    message = request.session.get('message', '')
    address = request.session.get('address', '')  # ✅ Always pulled here

    cart_items = []
    prices = {
        'espresso': 90,
        'latte': 120,
        'cappuccino': 110,
        'brownie': 70,
        'croissant': 80,
        'iced_mocha': 130,
    }

    for item, qty in cart.items():
        if qty > 0:
            cart_items.append({
                'name': item.replace('_', ' ').title(),
                'qty': qty,
                'price': prices[item],
                'subtotal': qty * prices[item]
            })

    if request.method == 'POST':
        method = request.POST.get('payment_method')

        # ✅ Save the complete order including address
        Order.objects.create(
            name=name,
            email=email,
            message=message,
            espresso=cart.get('espresso', 0),
            latte=cart.get('latte', 0),
            cappuccino=cart.get('cappuccino', 0),
            brownie=cart.get('brownie', 0),
            croissant=cart.get('croissant', 0),
            iced_mocha=cart.get('iced_mocha', 0),
            address=address,
            payment_method=method
        )

        return redirect('gpay' if method == 'gpay' else 'success')

    return render(request, 'cafe/payment.html', {
        'cart_items': cart_items,
        'total': total,
        'name': name
    })


def gpay(request):
    return render(request, 'cafe/gpay.html')


def success(request):
    return render(request, 'cafe/success.html')
