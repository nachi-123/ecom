from django.db import models
from django.utils.text import slugify 
class category(models.Model):
    # Slug field for URL-friendly names
    slug = models.SlugField(unique=True, max_length=100, null=True, blank=True)
    
    # Name of the category
    name = models.CharField(max_length=255,null=False,blank=True)
    
    # Image field to upload an image
    image = models.ImageField(upload_to='category_images/', null=False, blank=True)
    
    # Status to determine if category is active or not
    status = models.BooleanField(default=False,help_text="0=default,1=Hidden")
    
    # Trending field to indicate if the category is trending
    trending = models.BooleanField(default=False,help_text="0=default,1=Hidden")
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # If there's no slug, automatically generate it from the category name
            self.slug = slugify(self.name)
        super().save(*args, **kwargs) 

    # String representation of the category (for admin or debugging)
    def __str__(self):
        return self.name
      
    
    
    


class product(models.Model):
    c = models.ForeignKey(category, on_delete=models.CASCADE, related_name="products")
    slug = models.SlugField(unique=True, max_length=100, null=False, blank=True)
    name = models.CharField(max_length=255,null=False,blank=False)
    product_image = models.ImageField(upload_to='product_images/',null=False,blank=False)
    description = models.TextField(null=False,blank=False)
    quantity = models.PositiveIntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending = models.BooleanField(default=False,help_text="0=default,1=Hidden")

    def save(self, *args, **kwargs):
        if not self.slug:
            # If there's no slug, automatically generate it from the product name
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name