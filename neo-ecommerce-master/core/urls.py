from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    tarot,
    bioneuroemocion,
    pendulo,
    pendulohebreo,
    vidaspasadas,
    sanaciones,
    yoga,
    astrologia,
    runas
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('pags/sesiones/tarot.html/', tarot, name='tarot'),
    path('pags/sesiones/bioneuroemocion.html/', bioneuroemocion, name='bioneuroemocion'),
    path('pags/sesiones/pendulo.html/', pendulo, name='pendulo'),
    path('pags/sesiones/pendulohebreo.html/', pendulohebreo, name='pendulohebreo'),
    path('pags/sesiones/runas.html/', runas, name='runas'),
    path('pags/sesiones/vidaspasadas.html/', vidaspasadas, name='vidaspasadas'),
    path('pags/sesiones/sanaciones.html/', sanaciones, name='sanaciones'),
    path('pags/sesiones/yoga.html/', yoga, name='yoga'),
    path('pags/sesiones/astrologia.html/', astrologia, name='astrologia')





    ]
