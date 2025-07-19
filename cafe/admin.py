from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'payment_method', 'ordered_at', 'get_items', 'get_total']
    list_filter = ['payment_method', 'ordered_at']
    search_fields = ['name', 'email', 'address']

    def get_items(self, obj):
        items = []
        if obj.espresso: items.append(f"Espresso × {obj.espresso}")
        if obj.latte: items.append(f"Latte × {obj.latte}")
        if obj.cappuccino: items.append(f"Cappuccino × {obj.cappuccino}")
        if obj.brownie: items.append(f"Brownie × {obj.brownie}")
        if obj.croissant: items.append(f"Croissant × {obj.croissant}")
        if obj.iced_mocha: items.append(f"Iced Mocha × {obj.iced_mocha}")
        return ', '.join(items)
    get_items.short_description = 'Items Ordered'

    def get_total(self, obj):
        total = (
            obj.espresso * 90 +
            obj.latte * 120 +
            obj.cappuccino * 110 +
            obj.brownie * 70 +
            obj.croissant * 80 +
            obj.iced_mocha * 130
        )
        return f"₹{total}"
    get_total.short_description = 'Total Price'

admin.site.register(Order, OrderAdmin)
