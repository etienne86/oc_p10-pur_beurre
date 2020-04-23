import logging

from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import transaction
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserCreationForm, AuthenticationForm


logger = logging.getLogger(__name__)


@login_required
def account(request):
    context = {}
    # add the user to the context
    context['user'] = request.user
    return render(
        request,
        'auth/account.html',
        context,
    )


@login_required
def log_out(request):
    context = {}
    logout(request)
    return render(
        request,
        'auth/log_out.html',
        context,
    )


def sign(request):
    context = {}
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        authentication_form = AuthenticationForm(request, request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            email = user_creation_form.cleaned_data['email']
            password = user_creation_form.cleaned_data['password1']
            logger.info("Création du compte %s", email)
        if authentication_form.is_valid():
            email = authentication_form.cleaned_data['email']
            password = authentication_form.cleaned_data['password']
        if user_creation_form.is_valid() or authentication_form.is_valid():
            # log in the user
            with transaction.atomic():
                account = authenticate(email=email, password=password)
                if account is not None:
                    login(request, account)
            # redirect...
            if "?next=" in request.get_full_path():
                # ... either to the requested page
                return redirect(request.get_full_path().split("?next=")[1])
            else:
                # ... or to home page
                return redirect(reverse('off_sub:index'))
    else:  # GET request
        user_creation_form = UserCreationForm()
        authentication_form = AuthenticationForm()
    context['user_creation_form'] = user_creation_form
    context['authentication_form'] = authentication_form
    return render(
        request,
        'auth/sign.html',
        context
    )
