from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

# Submit item to bag using this view


def add_to_bag(request, item_id):
    """ Add a product of specific quantity to bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # get the bag variable if it exists in session or create if it does not.
    bag = request.session.get('bag', {})

    """ Structures the bag such that we can have a single item id for
    each item but still track multiple sizes. If the item is
    already in the bag, then we need to check if another item of the
     same id and same size already exists. And if so increment the
     quantity for that size and otherwise just set it equal to the quantity."""

    # See Django Project > data strcturing with sizing in OneNote
    if size:
        if item_id in list(bag.keys()):
            # item exists in bag in some form
            if size in bag[item_id]['items_by_size'].keys():
                # if existing size AND product, increase qty by one
                bag[item_id]['items_by_size'][size] += quantity
            else:
                # if existing product but different size
                bag[item_id]['items_by_size'][size] = quantity
        else:
            # item not yet in the bag
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
