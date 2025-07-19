from django.db import models

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('gpay', 'Google Pay'),
        ('cod', 'Cash on Delivery'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=True)
    address = models.TextField(blank=True, null=True)


    espresso = models.IntegerField(default=0)
    latte = models.IntegerField(default=0)
    cappuccino = models.IntegerField(default=0)
    brownie = models.IntegerField(default=0)
    croissant = models.IntegerField(default=0)
    iced_mocha = models.IntegerField(default=0)

    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='cod')
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.name} on {self.ordered_at.strftime('%d-%m-%Y %H:%M')}"
