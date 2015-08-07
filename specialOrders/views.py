"""
Definition of views.
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from Guru import urls


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )


def index(request):
    return HttpResponse("This is me testing stuffs out.")


def orders(request):
    from .models import Order
    order_list = Order.objects.all()
    context = {'order_list' : order_list}
    return render(request, 'app/orders.html', context)


def order_detail(request, order_id):
    from .models import Order
    detail = get_object_or_404(Order, pk=order_id)
    context = {'order_detail': detail}
    return render(request, 'app/detail.html', context)


def itemupdate(request):
    from .models import Order_item
    from django.utils import timezone
    # attempt to load an itemid from GET:
    try: 
        order_item = get_object_or_404(Order_item, pk=request.GET['id'])
    except(KeyError, Order_item.DoesNotExist):
        errors = ["view: itemupdate: No item was found with that order item ID."]
        context = {'errors': errors}
        return render(request, 'app/criticalerror.html', context)
    else:
        try:
            action = request.GET['action']
        except:
            errors = ["itemUpdateActionError: No action specified."]
            context = {'errors': errors}
            return render(request, 'app/criticalerror.html', context)
        else:
            # if we're toggling the is_picked_up flag on order_item...
            if action == 'fulfilled':
                order_item.item_picked_up = not order_item.item_picked_up
                order_item.save()
                success_message = "Item %s successfully updated." % order_item.item_sku
                return HttpResponseRedirect(reverse('detail', args=(order_item.item_order_id,)))
            else:
                return None

def item_manager(request):
    from .filters import ItemFilter
    from .models import Order_item
    f = ItemFilter(request.GET, queryset=Order_item.objects.all())

    context = {'filter' : f}

    return render(request, 'app/items.html', context)

def new_order_entry(request):
    from .models import Order, Order_item
    from .forms import OrderForm

    form = OrderForm
    context = {'form': form}
    return render(request, 'app/neworder.html', context)











