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
    from django.forms import formset_factory
    from .models import Vendor
    from .utils import order_validator
    from .forms import ItemOrderForm

    context = {}
    

    if request.method == "POST":
        if request.POST['add']:
            # Validate the supplied order info
            order_info = {
                'order_contact_name': request.POST['order_contact_name'],
                'order_contact_phone': request.POST['order_contact_phone'],
                'order_contact_email': request.POST['order_contact_email'],
            }
            ov = order_validator(order_info, items=None)
            if len(ov['errors']) > 0:
                context['errors'] = ov['errors']
            context['resub_order_info'] = ov['order_info']
            # Deal with items...
            ItemOrderFormset = formset_factory(ItemOrderForm, extra=2)
            item_formset = ItemOrderFormset(request.POST, request.FILES)
        elif request.POST['submit']:
            foo = 'bar'    
    else:
        ItemOrderFormset = formset_factory(ItemOrderForm, extra=2)
        item_formset = ItemOrderFormset()         

    context['item_formset'] = item_formset
    context['vendors'] = Vendor.objects.all()

    return render(request, 'app/neworder.html', context)

def new_order_submit(request):
    itemlist = request.POST.getlist('item')
    context = {'itemlist': itemlist}
    return render(request, 'app/neworder.html', context)









