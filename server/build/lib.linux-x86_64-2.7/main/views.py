# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
import json
#from django.http import Http404
#from django.shortcuts import get_object_or_404
from django.shortcuts import render
from contact import ContactForm
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import logging

from django.template import RequestContext

logger = logging.getLogger(__name__)


def index(request):
    return render_to_response(
        'app.html', {}, context_instance=RequestContext(request))


def partial_helper(request, template_name):
    """
    Provides access to Angular's routing
    :param request: not used
    :param template_name: The name of the partial template to render
    :return: rendered template
    """
    model = {
        'user': request.user,
        'authenticated': request.user.is_authenticated(),
    }
    return render_to_response(template_name, model)


@login_required
def all_users(request):
    """
    RESTFUL call to obtain a list of users
    :param request: Django request object
    :return: JSON data about all users, but really only will be
        populated with the name of the current user
    """

    data = [
        request.user.username,
    ]

    return_json = json.dumps(data)
    return HttpResponse(return_json, mimetype='application/json')


@login_required
@csrf_exempt
def current_user(request):
    """
    RESTFUL call to obtain information about the currently-logged in user, also
    provides information about how much of their email is currently imported.
    :param request: Django request object
    :return: JSON data about the current user
    """

    data = {
        'username': request.user.username,
        'email': request.user.email,
        'authenticated': request.user.is_authenticated(),
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'wp_url': request.user.get_profile().wp_url,
        'wp_username': request.user.get_profile().wp_url,
        'wp_password': request.user.get_profile().wp_password,
        'gmail_username': request.user.get_profile().gmail_username,
        'gmail_password': request.user.get_profile().gmail_password,
    }

    return_json = json.dumps(data)
    return HttpResponse(return_json, mimetype='application/json')


def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, "\
                    "please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render_to_response('auth.html', {
        'state': state, 'username': username
    })


def logout_view(request):
    """
    The user is requesting logout
    :param request:
    :return: Redirect to the opening page
    """
    logout(request)
    return HttpResponseRedirect('/')


def contact(request):
    if request.method == 'POST':  # If the form has been submitted...
        logger.info("codePOST condition")
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/polls/thanks/')
    else:
        logger.info("GET condition")
        form = ContactForm()  # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })


def thanks(request):
    return HttpResponse("Thanks.")
