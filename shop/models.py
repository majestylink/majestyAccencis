from django.db import models
from django.shortcuts import reverse
from core.helpers import LongUniqueId, getUniqueId
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.core.mail import send_mail
# Create your models here.


LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default=LongUniqueId, unique=True,)
    image = models.ImageField(verbose_name="Main Product Image")
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    # category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    category = models.ForeignKey('ProductCategory', blank=True, null=True, on_delete=models.SET_NULL)
    label = models.CharField(verbose_name="Product Label", max_length=10, blank=True, null=True)
    label_type = models.CharField(verbose_name="Product Label Type",choices=LABEL_CHOICES, default='P', max_length=1)
    description = models.TextField()
    inventory = models.PositiveIntegerField(help_text="How many of the Product are available", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    featured = models.BooleanField(help_text="If the Item should be featured on homepage",default=False)
    allow_request = models.BooleanField(default=True, help_text="If the Product is available for fashion Requests", )
    active = models.BooleanField(default=True)
    exclusive = models.BooleanField(default=False)

    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ["-timestamp", "-updated", "title"]

    def get_absolute_url(self):
        return reverse("shop:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("shop:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("shop:remove-from-cart", kwargs={
            'slug': self.slug
        })

    def get_price(self):
        try:
            if self.discount_price:
                price =self.discount_price
            else:
                price = self.price
        except Exception as e:
            price = self.price
        return price

    def amount_in_kobo(self):
        return self.get_price()*100

    def __str__(self):
        return self.title


class Colors(models.Model):
    title = models.CharField(max_length=50, unique=True)
    value = models.CharField(max_length=50, unique=True)
    products = models.ManyToManyField(Item, blank=True, related_name="colors")

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self):
        return self.title
TAG_CHOICE = (
    #TODO: add more colors
    ('purple', 'purple'),
    ('secondary', 'secondary'),
    ('danger', 'danger'),
    ('blue-text', 'blue-text'),
    ('cyan', 'cyan'),
    ('light-blue', 'light-blue'),
    ('yellow', 'yellow'),
    ('amber', 'amber'),
    ('light-green', 'light-green'),
    ('indigo', 'indigo'),
    ('lime', 'lime'),
    ('brown', 'brown'),
    ('orange', 'orange'),
    ('deep-orange', 'deep-orange'),
    ('deep-purple', 'deep-purple'),
    ('deep-purple', 'deep-purple'),

)

class Tags(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, default=getUniqueId)
    color = models.CharField(max_length=50, choices=TAG_CHOICE, default='purple')
    products = models.ManyToManyField(Item, blank=True, related_name="tags")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(help_text="Category Image", blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True, help_text="<b style='color:red'>Do Not Edit</b>", editable=True)
    products = models.ManyToManyField(Item, blank=True, related_name="categories")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["-timestamp", "-updated", "title"]

    def product_count(self):
        return self.products.all().count()

    def __str__(self):
        return self.title

def create_category_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = ProductCategory.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_category_slug(instance, new_slug=new_slug)
    return slug

def category_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_category_slug(instance)

pre_save.connect(category_pre_save_reciever, sender=ProductCategory)
def product_image_media_location(instance, filename):
    return "%s/%s" %(instance.product.slug, filename)


class ProductImage(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    media = models.ImageField(blank=True, null=True, 
                              upload_to=product_image_media_location)
    title = models.CharField(max_length=102, null=True, blank=True)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)

    def __str__(self):
        return str(self.media.name)



class OrderItem(models.Model):
    user = models.ForeignKey('core.UserProfile',
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
    user = models.ForeignKey('core.UserProfile',
                             on_delete=models.CASCADE, related_name="orders")
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'core.Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'core.Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-start_date",]
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return float(total)

    def amount_in_kobo(self):
        return self.get_total()*100

    def __str__(self):
        return str(self.user.user.username)



class Payment(models.Model):
    uid = models.CharField(default=getUniqueId, max_length=20, editable=False, help_text='Internal reference ID')
    user = models.ForeignKey('core.UserProfile',
                             on_delete=models.SET_NULL, blank=True, null=True,
                             related_name='payments')    
    reference = models.CharField(max_length=255, help_text="Reference from Paystack", blank=True, null=True,)
    transaction_id = models.CharField(max_length=255, help_text="Transaction from Paystack", blank=True, null=True,)
    message = models.CharField(max_length=255, help_text="Message from Paystack", blank=True, null=True,)
    # trxref = models.CharField(max_length=255, help_text="Trxref from Paystack", blank=True, null=True,)
    # trans = models.CharField(max_length=255, help_text="Trans from Paystack", blank=True, null=True,)
    status = models.CharField(max_length=255, help_text="Status string from Paystack", blank=True, null=True,)
    amount = models.DecimalField(max_digits=100, decimal_places=2, help_text='Amount Paid in Naira (₦)')
    success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, help_text="Transaction Date")

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ["-timestamp",]

    def __str__(self):
        return str(self.user.user.username)


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

    class Meta:
        verbose_name = "Discount Coupon"
        verbose_name_plural = "Discount Coupons"
        ordering = ["-timestamp",]
    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

    class Meta:
        verbose_name = "Refund"
        verbose_name_plural = "Requested Refunds"
        ordering = ["-timestamp",]
        
    def __str__(self):
        return f"{self.pk}"





class Fashioninsta(models.Model): #unique=True,
    user = models.ForeignKey('core.UserProfile', related_name='fashion_requests', on_delete=models.CASCADE,)
    slug = models.CharField(default=getUniqueId, unique=True, max_length=50, blank=True, null=True,  help_text="<b style='color:red'>Do Not Edit</b>", editable=False)
    product = models.ForeignKey(Item, related_name="requests", blank=True, null=True, on_delete=models.SET_NULL)
    neck = models.PositiveIntegerField(verbose_name="Neck", blank=True, null=True,)
    shoulder = models.PositiveIntegerField(verbose_name="Shoulder", blank=True, null=True,)
    chest = models.PositiveIntegerField(verbose_name="Chest", blank=True, null=True,)
    tommy = models.PositiveIntegerField(verbose_name="Tommy", blank=True, null=True,)
    sleeve = models.PositiveIntegerField(verbose_name="Sleeve Length", blank=True, null=True,)
    biceps = models.PositiveIntegerField(verbose_name="Biceps", blank=True, null=True,)
    round_sleeve = models.PositiveIntegerField(verbose_name="Round Sleeve", blank=True, null=True,)
    wrist = models.PositiveIntegerField(verbose_name="Cuff/Wrist", blank=True, null=True,)
    shirt = models.PositiveIntegerField(verbose_name="Shirt Length", blank=True, null=True,)
    trouser_waist = models.PositiveIntegerField(verbose_name="Trouser Waist", blank=True, null=True,)
    trouser_lenght = models.PositiveIntegerField(verbose_name="Trouser Lenght", blank=True, null=True,)
    hip = models.PositiveIntegerField(verbose_name="Sit/Hip", blank=True, null=True,)
    laps = models.PositiveIntegerField(verbose_name="Laps", blank=True, null=True,)
    knee = models.PositiveIntegerField(verbose_name="Knee", blank=True, null=True,)
    calf = models.PositiveIntegerField(verbose_name="Calf", blank=True, null=True,)
    ankle = models.PositiveIntegerField(verbose_name="Base/Ankle", blank=True, null=True,)
    description = models.TextField(max_length=350, blank=True, null=True)	
    timestamp = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    done = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Fashion Request"
        verbose_name_plural = "Fashion Requests"
        ordering = ["-timestamp"]


    def __str__(self):
        return str(self.slug)


def mailOrder(sender, instance, created, *args, **kwargs):
    msg = ''' 
            Dear {0},
            Thank You for Your Fashion Requests. Find The Details of the Order Below:
            Reference Code = {1}
            Product = {2}
            Product Code: {22}
            Neck Measurement = {3}
            Shoulder Measurement = {4}
            Chest Measurement = {5}
            Tommy Measurement = {6}
            Sleeve Measurement = {7}
            Biceps Measurement = {8}
            Round_sleeve Measurement = {9}
            Wrist Measurement = {10}
            Shirt Measurement = {11}
            Trouser Waist Measurement = {12}
            Trouser Lenght Measurement = {13}
            Sit/Hip Measurement = {14}
            Laps Measurement = {15}
            Knee Measurement = {16}
            Calf Measurement = {17}
            Base/Ankle Measurement = {18}
            Note = {19}
            Time Recorded = {20}
            Status: {21}

          '''.format(
                instance.user, 
                instance.slug, 
                instance.product,
                instance.neck, 
                instance.shoulder, 
                instance.chest, 
                instance.tommy, 
                instance.sleeve, 
                instance.biceps, 
                instance.round_sleeve, 
                instance.wrist, 
                instance.shirt, 
                instance.trouser_waist, 
                instance.trouser_lenght, 
                instance.hip, 
                instance.laps, 
                instance.knee, 
                instance.calf, 
                instance.ankle, 
                instance.description, 
                instance.timestamp, 
                # instance.updated, 
                'Ready' if instance.done else 'Processing',
                instance.product.slug,
                # instance.done,  
          )
    mailler = 'info@accencis.biz'
    subject = 'Fashion Request  || Accencis'
    managers = ['ahmad@dabolinux.com']
    receivers = managers + [instance.user.user.email]
    try:
        send_mail(subject,msg, mailler, receivers, fail_silently=False, )
    except Exception as e:
        print(e)

post_save.connect(mailOrder, Fashioninsta)