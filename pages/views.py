from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import *
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing_FK.objects.order_by('-list_date')[:3]
    for rate in listings:
        rate.image = rate.image.strip('][').split(', ')
        if rate.retail_price:
            rate.retail_price = float(rate.retail_price)
        else:
            rate.retail_price = 0
        rate.is_FK_Advantage_product = eval(rate.is_FK_Advantage_product.title())
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)

