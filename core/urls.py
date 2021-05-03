from django.urls import path, include
from .views import HomeView,SanphamView,Index,HomeVieww
from django.conf import settings
from django.conf.urls.static import static
from . import views as core_view
from profiles import views as profiles_views


urlpatterns = [
    path('sanpham/',SanphamView.as_view(), name = 'sanpham'),
    path('sanphamcuthe/<int:sanpham_id>',Index.as_view(), name = 'sanphamcuthe' ),
    path('sanpham/<int:loaisp_id>', core_view.loaispview, name = "loc_loaisp" ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('giohang/',core_view.giohangview , name = 'giohang'),
    path('',HomeView.as_view(), name = 'Trangchu'),
    path('home/',HomeVieww.as_view(), name = 'trangchu'),
    path('login/', core_view.SiteLoginView.as_view(), name = 'login'),
    path('register/', core_view.register, name = 'register'),
    path('banchay/', core_view.banchayview, name = 'banchay'),
    path('diemcao/', core_view.diemcaoview, name = 'diemcao'),
    path('giamdan/', core_view.giamdanview, name = 'giamdan'),
    path('tangdan/', core_view.tangdanview, name = 'tangdan'),
    path('user/',core_view.userview, name = 'user')
    path('profile/',HomeVieww.as_view(),name = 'profile'),
    path('cart/add/<int:id>/', core_view.cart_add, name='cart_add'),
    #path('cart/item_clear/<int:id>/', core_view.item_clear, name='item_clear'),
    #path('cart/item_increment/<int:id>/',core_view.item_increment, name='item_increment'),
    #path('cart/item_decrement/<int:id>/',core_view.item_decrement, name='item_decrement'),
    #path('cart/cart_clear/', core_view.cart_clear, name='cart_clear'),
    #path('cart/cart-detail/',core_view.cart_detail,name='cart_detail'),
   
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)