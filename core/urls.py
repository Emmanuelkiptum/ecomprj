from django.urls import path, include
from core.views import index
from core.views import category_list_view, product_list_view, category_product_list__view, vendor_list_view, vendor_detail_view, product_detail_view, tag_list, ajax_add_review, search_view, filter_product, add_to_cart, cart_view, delete_item_from_cart, update_cart, payment_completed_view, payment_failed_view, customer_dashboard, order_detail, wishlist_view, make_address_default, add_to_wishlist, remove_wishlist, contact, ajax_contact_form, save_checkout_info, create_checkout_session, checkout

app_name = "core"

urlpatterns = [
    # Homepage
      path("", index, name="index"),
      path("products/", product_list_view, name="product-list"),
      path("product/<pid>/", product_detail_view, name="product-detail"),
    # Category
      path("category/", category_list_view, name="category-list"),
      path("category/<cid>/", category_product_list__view, name="category-product-list"),
    # Vendor
      path("vendors/", vendor_list_view, name="vendor-list"),
      path("vendor/<vid>/", vendor_detail_view, name="vendor-detail"),
      
    # Tags
      path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),
      
       # Add Review
    path("ajax-add-review/<int:pid>/", ajax_add_review, name="ajax-add-review"),
    
     # Search
    path("search/", search_view, name="search"),
    #Filter products
    path("filter-products/", filter_product, name="filter-product"),
    
    #Add to cart
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    path("cart/", cart_view, name="cart"),
    #Delete from cart
    path("delete-from-cart/", delete_item_from_cart, name="delete-from-cart"),
    
    # Update  Cart
    path("update-cart/", update_cart, name="update-cart"),
      #  checkout
    path("api/create_checkout_session/<oid>/", create_checkout_session, name="api_checkout_session"),
    path("save_checkout_info/", save_checkout_info, name="save_checkout_info"),
    path("checkout/<oid>/", checkout, name="checkout"),
    
    
    path('paypal/', include('paypal.standard.ipn.urls')),
     
    path("payment-completed/<oid>/", payment_completed_view, name="payment-completed"),
    path("payment-failed/", payment_failed_view, name="payment-failed"),
        # Dashboard URL
    path("dashboard/", customer_dashboard, name="dashboard"),
    
        # Order Detail URL
    path("dashboard/order/<int:id>", order_detail, name="order-detail"),
    
      # Making address default
    path("make-default-address/", make_address_default, name="make-default-address"),
    
        # wishlist page
    path("wishlist/", wishlist_view, name="wishlist"),
    
        # adding to wishlist
    path("add-to-wishlist/", add_to_wishlist, name="add-to-wishlist"),
    
        # Removing from wishlist
    path("remove-from-wishlist/", remove_wishlist, name="remove-from-wishlist"),
    
    path("contact/", contact, name="contact"),
    
  path("ajax-contact-form/", ajax_contact_form, name="ajax-contact-form"),
    
]