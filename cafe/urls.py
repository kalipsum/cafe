from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from cafe.pkg.register.views import home
from cafe.pkg.register.views import logout
from cafe.pkg.register.views import auth_v
from cafe.pkg.register.views import loggedin, confirm, register
from cafe.pkg.register.views import invalid_l, login, reset_confirm, reset
from cafe.pkg.kitchen.views import menu
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cafe.pkg.kitchen.views import menu_items, dish, filter_dishes
from cafe.pkg.orders.views import order, basket, basket_add, clean, orders

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Cafeshka.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^accounts/login/', login, name='loginN'),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/auth/$', auth_v),
    url(r'^accounts/loggedin/$', loggedin),
    url(r'^accounts/invalid/$', invalid_l),
    url(r'^confirm/(?P<activation_key>\w+)/', confirm,),
    url(r'^register/$', register, name='register'),
    url(r'^reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', reset_confirm, name='auth_password_reset_confirm'),
    url(r'^reset/$', reset, name='reset'),
    url(r'^menu/$', menu),
    url(r'^menu/(?P<menu_id>\d+)/?$', menu_items),
    url(r'^dish/(?P<dish_id>\d+)/?$', dish),
    url(r'^dish/filter/?.*$', filter_dishes),
    url(r'^make/orders/', order),
    url(r'^orders/$', orders),
    url(r'^add/basket/$', basket_add),
    url(r'^basket/?.*$', basket),
    url(r'^clean/basket/$', clean),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


