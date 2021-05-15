from django import template
from shop.models import Order

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        profile = user.profile
        qs = Order.objects.filter(user=profile, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0
