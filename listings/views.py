from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

from .models import *

def index(request):
  listings = Listing_FK.objects.order_by('-list_date')[:100]
  total_rate = 0
  for rate in listings:
    rate.image = rate.image.strip('][').split(', ')
    if rate.retail_price:
      rate.retail_price = float(rate.retail_price)
    else:
      rate.retail_price = 0
    rate.is_FK_Advantage_product = eval(rate.is_FK_Advantage_product.title())
  paginator = Paginator(listings, 20)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)
  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing_FK, pk=listing_id)
  listing.image = listing.image.strip('][').split(', ')
  if listing.retail_price:
    listing.retail_price = float(listing.retail_price)
  else:
    listing.retail_price = 0
  listing.is_FK_Advantage_product = eval(listing.is_FK_Advantage_product.title())
  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

def search(request):
  queryset_list = Listing_FK.objects.order_by('-list_date')[:100]

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

    # Price
  if 'price' in request.GET:
    price = request.GET['price']
    price = str(float(price)//70)
    if price:
      queryset_list = queryset_list.filter(discounted_price__lte=price)
  for rate in queryset_list:
    rate.image = rate.image.strip('][').split(', ')
    if rate.retail_price:
      rate.retail_price = float(rate.retail_price)
    else:
      rate.retail_price = 0
    rate.is_FK_Advantage_product = eval(rate.is_FK_Advantage_product.title())
  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)
