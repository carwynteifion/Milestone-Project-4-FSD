from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)

from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    format = None
    if 'product_format' in request.POST:
        format = request.POST['product_format']
    bag = request.session.get('bag', {})

    if format:
        if item_id in list(bag.keys()):
            if format in bag[item_id]['is_book'].keys():
                bag[item_id]['is_book'][format] += quantity
                messages.success(
                    request, (
                        f'Updated format {format.upper()} {product.name} '
                        f'quantity to {bag[item_id]["is_book"][format]}'
                    ),
                    extra_tags='bag'
                )
            else:
                bag[item_id]['is_book'][format] = quantity
                messages.success(
                    request,
                    f'Added format {format.upper()} {product.name} to the bag',
                    extra_tags='bag'
                )
        else:
            bag[item_id] = {'is_book': {format: quantity}}
            messages.success(
                request,
                f'Added format {format.upper()} {product.name} to the bag',
                extra_tags='bag'
            )
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}',
                extra_tags='bag'
            )
        else:
            bag[item_id] = quantity
            messages.success(
                request, f'Added {product.name} to your bag', extra_tags='bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    format = None
    if 'product_format' in request.POST:
        format = request.POST['product_format']
    bag = request.session.get('bag', {})

    if format:
        if quantity > 0:
            bag[item_id]['is_book'][format] = quantity
            messages.success(
                request, (
                    f'Updated format {format.upper()} {product.name} '
                    f'quantity to {bag[item_id]["is_book"][format]}'
                ),
                extra_tags='bag'
            )
        else:
            del bag[item_id]['is_book'][format]
            if not bag[item_id]['is_book']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed format {format.upper()} {product.name} from the bag',
                extra_tags='bag'
            )
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}',
                extra_tags='bag'
            )
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from your bag',
                extra_tags='bag'
            )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        format = None
        if 'product_format' in request.POST:
            format = request.POST['product_format']
        bag = request.session.get('bag', {})

        if format:
            del bag[item_id]['is_book'][format]
            if not bag[item_id]['is_book']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed format {format.upper()} {product.name} from the bag',
                extra_tags='bag'
            )
        else:
            bag.pop(item_id)
            messages.success(
                request,
                f'Removed {product.name} from your bag', extra_tags='bag'
            )

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}', extra_tags='bag')
        return HttpResponse(status=500)
