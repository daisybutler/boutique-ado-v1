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

    # get the bag variable if it exists in session or create if it does not.
    bag = request.session.get('bag', {})

    # Add the item to the bag or update the quantity if it already exists.
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    # Overwrite the variable in the session with the updated version
    request.session['bag'] = bag
    return redirect(redirect_url)
