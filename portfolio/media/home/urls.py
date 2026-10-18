from django.urls  import path
from.import views
urlpatterns=[
    path("",views.index,name="index"),
    path("newarrivals/",views.newarrivals,name="newarrivals"),
    path("product/",views.product,name="product"),
    path("card/",views.card,name="card"),
    path("add_to_cart/<int:product_id>/",views.add_to_cart,name="add_to_cart"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("plus/<int:card_id>/",views.plus,name="plus"),
    path("minus/<int:card_id>/",views.minus,name="minus"),
    path("delete_card/<int:card_id>/",views.delete_card,name="delete_card"),
    path("checkout/",views.checkout,name="checkout"),
    path("logout/",views.logout,name="logout"),
    path("wishlist/<int:pk>/",views.wishlist,name="wishlist"),
    path("wishlistpage/",views.wishlistpage,name="wishlistpage"),
    path("wishlist_delete/<int:pk>/",views.wishlist_delete,name="wishlist_delete"),
    path("thankyou/",views.thankyou,name="thankyou"),
]
