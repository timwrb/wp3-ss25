from django.contrib import admin
from shoppingcart.models import Customer

# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "email", "display_password_strength"]
    # fields = ["email", "password"]
    '''fieldsets = [
        ("Basisdaten", {"fields": ["user__firstname", "user__lastname", "email"]}),
         ("Kundendetails", {"fields":["salutation", "birthday","user__password"]})
    ]'''

    def display_password_strength(self, obj):
        if len(obj.user.password)>2:
            return True
        else:
            return False

    display_password_strength.short_description = "Passwortsicherheit"
    display_password_strength.boolean = True


admin.site.register(Customer, AdminCustomer)
