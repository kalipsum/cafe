from django.conf.urls import patterns, include, url
from django.contrib import admin
from register.views import home
from register.views import login
from register.views import logout
from register.views import auth_v
from register.views import loggedin
from register.views import invalid_l
from django.views.generic import RedirectView
import register.views

from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Cafeshka.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^accounts/login/',  'register.views.login', name='loginN'),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/auth/$', auth_v),
    url(r'^accounts/loggedin/$', loggedin),
    url(r'^accounts/invalid/$', invalid_l),
    url(r'^confirm/(?P<activation_key>\w+)/', register.views.confirm),
    url(r'^register/$', register.views.register, name='register'),
    url(r'^reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
            'register.views.reset_confirm', name='reset_confirm'),
    url(r'^reset/$', 'register.views.reset', name='reset'),

)
