"""Platzigram views module."""
#Django

from turtle import pd
from django.http import HttpResponse

#utulitis
from datetime import date, datetime
import json
def hello(request):
    now =  datetime.now().strftime('%b,%dth, %Y -%H:%M hrs')
    
    return HttpResponse(f'Oh, hi! Current server time is {now}')

def sorted_integer(request):
    """" Retunr a Json resposne  with sorted integers."""
    # import pdb; pdb.set_trace()
    numbers =  [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status':'ok',
        'numbers': sorted_ints,
         'message': 'Integers sorted succesfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )
    
def say_hi(request,name, age):
    """Return a greeting"""
    if age < 12:
        message = f"Sorry {name}, you are not allowed here"
    else:
        message = f"Hello, {name}! Welcome to Platzigram"
    return HttpResponse(message)
     