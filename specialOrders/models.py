from django.db import models

"""
Definition of models.
"""

from django.db import models

class Order(models.Model):
    order_date = models.DateField()
    order_contact_name = models.CharField(max_length=75)
    order_contact_phone = models.IntegerField(null=True)
    order_contact_email = models.EmailField(null=True, blank=True)
    order_is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.order_contact_name

    def is_pending(self):
        if(len(self.order_item_set.filter(item_ordered=0)) > 0):
            return True
        else:
            return False

    def is_ordered(self):
        if(len(self.order_item_set.filter(item_ordered=1)) == self.order_item_set.count() ):
            return True
        else:
            return False

    def is_arrived(self):
        if(len(self.order_item_set.filter(item_arrived=1)) == self.order_item_set.count() ):
            return True
        else:
            return False

    def is_complete(self):
         if(len(self.order_item_set.filter(item_picked_up=1)) == self.order_item_set.count() ):
            return True
         else:
            return False

    def resolve_status(self):
        if(self.is_complete()):
            return "complete"
        elif(self.is_arrived()):
            return "arrived"
        elif(self.is_ordered()):
            return "ordered"
        else: return "pending"

    def determine_item_status(self):
        numitems = len(self.order_item_set.all())
        if len(self.order_item_set.filter(item_picked_up=1)) == numitems:
            return 'fulfilled'
        elif len(self.order_item_set.filter(item_arrived=1)) == numitems:
            return 'arrived'
        elif len(self.order_item_set.filter(item_ordered=1)) == numitems:
            return 'ordered'
        elif len(self.order_item_set.filter(item_ordered=0)) == numitems:
            return 'outstanding'
        else:
            return 'mixed'


class Vendor(models.Model):
    vendor_sap_id = models.IntegerField(primary_key=True)
    vendor_name = models.CharField(max_length=50)
    vendor_availability = models.CharField(max_length=1000)

    def __str__(self):
        return self.vendor_name


class Order_item(models.Model):
    item_order = models.ForeignKey(Order)
    item_vendor = models.ForeignKey(Vendor)
    item_sku = models.IntegerField()
    item_descr = models.CharField(max_length=40)
    item_qty = models.IntegerField()
    item_paid = models.BooleanField(default=False)
    item_ordered = models.BooleanField(default=False)
    item_ordered_date = models.DateField(null=True, blank=True)
    item_ordered_po = models.IntegerField(null=True, blank=True)
    item_arrived = models.BooleanField(default=False)
    item_arrived_date = models.DateField(null=True, blank=True)
    item_picked_up = models.BooleanField(default=False)
    item_picked_up_date = models.DateField(null=True, blank=True)

    def resolve_status(self):
        if (self.item_picked_up):
            return "fulfilled"
        elif(self.item_arrived):
            return "arrived"
        elif(self.item_ordered):
            return "ordered"
        else:
            return "pending"

    def __str__(self):
        return str(self.item_sku)



