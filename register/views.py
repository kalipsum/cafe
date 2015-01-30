
from django.contrib import auth
from django.core.context_processors import csrf

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from register.forms import *
from register.models import *
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
from register.forms import RegistrationForm, LoginForm
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm
from kitchen.models import Menu, Dish


menu_list = Menu.objects.all()


def home(request):
    return render_to_response('home.html', {'menu_list': menu_list})


def login(request):
    a = {}
    a.update(csrf(request))
    return render_to_response('login.html', a)


def auth_v(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    return render_to_response('loggedin.html',{'fullname':request.user.username}, {'dish_list': dish_list})


def invalid_l(request):
    return render_to_response('invalid.html')


def logout(request):
    auth.logout(request)
    return render_to_response('home.html')

def register(request):
#if request.user.is_authenticated():
# They already have an account; don't let them register again
    #    return render_to_response('core/register.html', {'has_account': True})
    if request.method == 'GET':
        c = {}
        c.update(csrf(request))
        c['form'] = RegistrationForm()
        return render_to_response('register.html', c)

    if not request.method == 'POST': return HttpResponseRedirect('/')
    registrationForm = RegistrationForm(request.POST)
    if registrationForm.is_valid():
        user = registrationForm.save(commit=False)
        user.is_active = False
        user.save()
        profile = UserProfile(user=user,
                              activation_key=hashlib.sha224((user.username).encode('utf8')).hexdigest()[:40],
                              key_expires=datetime.datetime.today() + datetime.timedelta(days=2),

        )
        profile.save()


        host = request.META['SERVER_NAME']
        email_subject = 'Welcome!'
        email_body = """Thanks for signing up.  To activate your account, follow this link: http://%(host)s/accounts/confirm/%(hash)s"""
        email_body = email_body % {'host': host, 'hash':profile.activation_key}

        send_mail(email_subject, email_body, 'account_creator@' + host, [user.email])
        return render_to_response('register.html', {'created': True})
    c = {}
    c.update(csrf(request))
    c['form'] = registrationForm
    return render_to_response('register.html', c)


def confirm(request, activation_key):
    if request.user.is_authenticated():
        return render_to_response('confirm.html', {'has_account': True})
    user_profile = get_object_or_404(UserProfile,
                                     activation_key=activation_key)
    if user_profile.key_expires < datetime.datetime.today():
        return render_to_response('confirm.html', {'expired': True})
    user_account = user_profile.user
    user_account.is_active = True
    user_account.save()
    return render_to_response('confirm.html', {'success': True})


def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='password_reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('loginN'))


def reset(request):
    return password_reset(request, template_name='password_reset_form.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt',
        post_reset_redirect=reverse('loginN'),
)