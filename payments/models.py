from django.utils import timezone
from django.db import models
from commons import models as cmn_models
from users import models as u_models
import os

"""Payments may be approved automatically by the system or manually by the admins. Payments that are not approved 
    will be publicised. Cash, mobile, and bank payments must be approved by administrators for decreasing fraud 
    transactions, while credit card, voucher and subscription payments will be approved by the system automatically."""
class PaymentApprovalMode(models.Model):
    mode = models.CharField(verbose_name="Payment approval mode", max_length=20, default="MANUAL", blank=False, null=False)
    description  = models.TextField(null=True, blank=True)

    def __STR__(self):
        return self.approval_mode


"""A payment method that users use for paying for services that they get from the system. For instance, 
    agents must pay for listing a property. Users may use any of the payment methods available in the system, 
    such as credit card payment, bank payment, voucher payment, subscription payment, etc. """
class PaymentMethod(models.Model):
    name = models.CharField(verbose_name="Payment method name", max_length=30, null=False, blank=False)
    approval_mode = models.ForeignKey(PaymentApprovalMode, on_delete=models.CASCADE, verbose_name="Payment method name")
    description  = models.TextField(null=True, blank=True)

    def __STR__(self):
        return self.name

"""A payment method discount is a discount applied to a specific payment method for using that payment method"""
class PaymentMethodDiscount(models.Model):
    payment_method = models.OneToOneField(PaymentMethod, on_delete=models.CASCADE)
    discount_percentage = models.FloatField(verbose_name="discount in percent", default=0.00)
    discount_fixed = models.FloatField(verbose_name="discount amount discount", default=0.00)
    added_on = models.DateTimeField(verbose_name="date added", default=timezone.now, editable=False)
    start_on = models.DateTimeField(verbose_name="date discount starts", default=timezone.now, editable=False)
    expire_on = models.DateTimeField(verbose_name="date discount expires", null=False, blank=False, editable=False)
    narative = models.TextField(null=True, blank=True)

    def __str__(self):
        return "discount percentage = %s, discount fixed = %s" % (self.discount_percentage, self.discount_fixed)


"""Payment information for a specific service. The user selects a specific payment method for payment. """
class Payment(models.Model): 
    payment_method = models.ManyToManyField(PaymentMethod, through="PaymentByMethod", verbose_name="payment method used")
    total_price = models.FloatField(verbose_name="total price to be paid", default=0.00)
    paid_amount = models.FloatField(verbose_name="paid amount", default=0.00)

    @property
    def left_amount(self):
        return self.total_price - self.paid_amount

    narative = models.TextField(blank=True, null=True)

    
    def get_is_approved_default(self):
       if self.payment_method.approval_mode.mode == "AUTO":
           return True
       else:
            return False

    is_approved = models.BooleanField(default=get_is_approved_default)

    def __str__(self):
        return self.total_price


"""Payment can be done with one or more methods. For instance, a portion of the rice can be covered 
    through vouchers whole the rest could be covered by credit card payment"""
class PaymentByMethod(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, verbose_name="parent payment")
    method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, verbose_name="payment method")
    amount = models.FloatField(verbose_name="payment amount using this method", default=0.00)
    paid_on = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "payment method = %s, payment amount %d" % (self.method.name, self.amount)


def get_bank_reciept_file_path(instance, filename):
    now = timezone.now()
    basename, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond//1000
    return f"payments/static/media/bank/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

def get_mobile_reciept_file_path(instance, filename):
    now = timezone.now()
    basename, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond//1000
    return f"payments/static/media/mobile/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"



"""A user may pay the payment through a bank transfer. In this case, the user must receive the 
    receipt from the bank and attach it to the system."""
class BankPayment(models.Model):
    parent_payment = models.OneToOneField(Payment, on_delete=models.CASCADE, verbose_name="parent payment record")
    bank_name = models.CharField(verbose_name="cash acceptor bank name", max_length=100, null=False, blank=False)
    bank_branch_name = models.CharField(null=True, blank=True, max_length=100)
    txn_reference_number = models.CharField(verbose_name="transaction reference name", max_length=50, null=False, blank=False)
    paid_on = models.DateTimeField(default=timezone.now, editable=True)
    bank_city = models.ForeignKey(cmn_models.City, on_delete=models.SET_NULL, null=True)
    bank_region= models.ForeignKey(cmn_models.Region, on_delete=models.SET_NULL, null=True)
    bank_country = models.ForeignKey(cmn_models.Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "bank reference number = %s, paid at bank = %s" % (self.txn_reference_number, self.bank_name)


"""A user must attach a bank receipt after paying the payment through the bank."""
class BankReciept(models.Model):
    bank_payment = models.ForeignKey(BankPayment, on_delete=models.CASCADE)
    reciept = models.FileField(verbose_name="bank reciept path", upload_to=get_bank_reciept_file_path)
    uploaded_on = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.reciept



"""A user may pay the payment for a service through mobile banking. In this case, 
    the user must attach the mobile payment receipt to the system after payment"""
class MobilePayment(models.Model):
    parent_payment = models.OneToOneField(Payment, on_delete=models.CASCADE, verbose_name="parent payment record")
    mobile_app_name = models.CharField(max_length=50, null=False, blank=False)
    txn_reference_number = models.CharField(verbose_name="transaction reference number", max_length=50, null=False, blank=False)
    paid_on = models.DateTimeField(default=timezone.now, editable=True)

    def __STR__(self):
        return "txn reference number = %s, mobile name = %s" % (self.txn_reference_number, self.mobile_app_name)


"""A user must attach a bank receipt after paying the payment through the bank."""
class MobilePayReciept(models.Model):
    mobile_payment = models.ForeignKey(MobilePayment, on_delete=models.CASCADE)
    reciept = models.FileField(verbose_name="mobile reciept path", upload_to=get_mobile_reciept_file_path)
    uploaded_on = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.reciept


"""Card types that are supported by the system for online payment, such as Visa, Master Card, etc"""
class SupportedCardScheme(models.Model):
    scheme_name = models.CharField(verbose_name="card scheme name", max_length=50, null=False, blank=False)
    BIN = models.CharField(verbose_name="card BIN", max_length=10, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.scheme_name


"""A user may use his acceptable credit card to pay the payment. This is the easiest way of payment method available. """
class CreditCardPayment(models.Model):
    parent_payment = models.OneToOneField(Payment, on_delete=models.CASCADE, verbose_name="parent payment record")
    card_scheme = models.ForeignKey(SupportedCardScheme, on_delete=models.SET_NULL, null=True, verbose_name="parent card scheme", related_name="scheme_payment")
    txn_reference_number = models.CharField(verbose_name="transaction reference number", max_length=50, null=False, blank=False)
    card_holder_name = models.CharField(verbose_name="card holder name", max_length=30, null=True, blank=True)
    card_last_4_digits =  models.CharField(max_length=4, null=True, blank=True)
    card_issuer = models.CharField(verbose_name="card issuer bank name", max_length=100, null=True, blank=True)
    paid_on = models.DateTimeField(default=timezone.now, editable=True)

    def __str__(self):
        return "transaction reference number = %s, card last 4 digit = %s" % (self.txn_reference_number, self.card_last_4_digits)


"""A user may alternatively pay the payment through cash payment at payment points. This method is the least preferable
     method by can be used whenever appropriate"""
class CashPayment(models.Model):
    parent_payment = models.OneToOneField(Payment, on_delete=models.CASCADE, verbose_name="parent payment record")
    cash_reciever_admin = models.ForeignKey(u_models.SystemAdmin, on_delete=models.SET_NULL, null=True)
    recieved_cash_amount = models.FloatField(default=0.00)
    recieved_on = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "%d recieved on %s" % (self.recieved_cash_amount, self.recieved_on)

"""A coupon is a ticket with a unique code that has a specific value and is redeemed for 
    discount, refund, or other purposes"""
class Coupon(models.Model):
    code = models.CharField(verbose_name="coupon code", unique=True, max_length=20, null=False, blank=False)
    initial_value = models.FloatField(verbose_name="initial coupon value", default=0.00)
    current_value = models.FloatField(verbose_name="current coupon value", default=0.00)
    redeemed_on = models.DateTimeField(verbose_name="redemption date", default=timezone.now, editable=False)
    expire_on = models.DateTimeField(verbose_name="expire date", editable=True)
    
    @property
    def status(self):
        if timezone.now > self.expire_on:
            return "EXPIRED"
        else:
            return "ACTIVE"

    def __str__(self):
        return self.code


"""A user may use a coupon to pay the payment for a service. The coupon can 
    be used to cover partial or full-service fees"""
class CouponPayment(models.Model):
    coupon = models.ManyToManyField(Coupon, through="AppliedCoupon")
    parent_payment = models.OneToOneField(Payment, on_delete=models.CASCADE, verbose_name="parent payment record")
    paid_amount = models.FloatField(verbose_name="paid_amount", default=0.00)
    paid_on = models.DateTimeField(verbose_name="payment date", default=timezone.now, editable=True)


"""Association table between Coupon and Coupon Payment"""
class AppliedCoupon(models.Model):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    coupon_payment = models.ForeignKey(CouponPayment, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(default=timezone.now, editable=False)

