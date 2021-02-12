from rest_framework import serializers

from listings.models import *

class ListingSerializer(serializers.ModelSerializer ): # forms.ModelForm
    class Meta:
        model = Listing
        fields = [
            'realtor',
            'id',
            'title',
            'address',
            'city',
            'state',
            'zipcode',
            'description',
            'price', 
            'bedrooms', 
            'bathrooms',
            'garage',
            'sqft', 
            'lot_size', 
            'photo_main', 
            'photo_1',
            'photo_2',
            'photo_3',
            'photo_4', 
            'photo_5',
            'photo_6',
            'is_published',
            'list_date',         
        ]
        read_only_fields = ['user']
        # Converts to JSON
        # validations for data passed 
    
    def validate_title(self, value):
        qs = Listing.objects.filter(title__iexact=value) # including instance
        if self.instance:
            qs = qs.exlude(pk=self.instance.pk) 
        if qs.exists():
            raise serializers.ValidationError("The Listing must be unique")
        return value


class ListingFKSerializer(serializers.ModelSerializer):  # forms.ModelForm
    class Meta:
        model = Listing_FK
        fields = [
            'uniq_id',
                    'crawl_timestamp',
                    'product_url',
                    'product_name',
                    'product_category_tree',
                    'pid',
                    'retail_price',
                    'discounted_price',
                    'image',
                    'is_FK_Advantage_product',
                    'description',
                    'product_rating',
                    'overall_rating',
                    'brand',
                    'product_specifications',
            'list_date'
        ]
        read_only_fields = ['user']
        # Converts to JSON
        # validations for data passed

    def validate_title(self, value):
        qs = Listing_FK.objects.filter(product_name__iexact=value)  # including instance
        if self.instance:
            qs = qs.exlude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The Listing must be unique")
        return value