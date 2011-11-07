from Tsoha.models import Drink
from Tsoha.forms import SearchForm
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    
def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
    })
    
def save_test(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = form.cleaned_data['parameter']
            message = form.cleaned_data['target']
            print subject
            print message
            return HttpResponse("Posting was succeess") # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return HttpResponse("Posting was failure") 
