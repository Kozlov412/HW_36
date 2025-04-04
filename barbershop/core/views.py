from django.shortcuts import render

def landing(request):
    return render(request, 'landing.html')

def thanks(request):
    return render(request, 'core/thanks.html')

def orders_list(request):
    orders = [
        # Ваши данные заявок
    ]
    return render(request, 'core/orders_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    return render(request, 'core/order_detail.html', {'order': order})
