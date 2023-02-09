from django.shortcuts import redirect


"""Método login_redirect para logearse despues de registrarse"""
def login_redirect(request):
    return redirect('/account/login')