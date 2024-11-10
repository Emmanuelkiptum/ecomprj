from core.models import CartOrderItems, Product, Category, Vendor, CartOrder, ProductImages, ProductReview, wishlist, Address
from django.contrib.auth.models import AnonymousUser

def default(request):
    categories = Category.objects.all()

    # Check if the user is authenticated
    if isinstance(request.user, AnonymousUser):
        address = None  # Handle case for unauthenticated users
    else:
        try:
            address = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            address = None  # Handle case when no address is found for the user

    return {
        'categories': categories,
        'address': address,
    }
