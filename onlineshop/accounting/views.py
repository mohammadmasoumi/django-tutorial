from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action
# install python docstring
# install python linter

def say_hello(request):
    """a sample request handler

    Args:
        request ([type]): [description]
    """

    # Fetch data from database
    # Transfor data
    # Send email
    # ...

    return HttpResponse('Hello World')


def say_hello_with_template(request):
    """[summary]

    Args:
        request ([type]): [description]
    """

    return render(request, 'hello.html', {'name': 'Mohammad'})