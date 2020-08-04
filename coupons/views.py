from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from .models import *

def IndexView(request):
    context = {}
    if request.method == "GET":
        context["all_coupons_list"] = Coupon.objects.all()
    return render(request, 'index.html', context=context)

@login_required
def DetailsView(request, pk):
    context = {}

    #Retrieve coupon_instance
    coupon_instance = get_object_or_404(Coupon, pk=pk)
    context["object"] = coupon_instance
    context["redeem_success"] = 0

    #Redemption submission
    if request.method == "POST":
        try:
            coupon_instance.active = False
            coupon_instance.save()
            context["redeem_success"] = 1
        except:
            context["redeem_success"] = 2
        #finally:
            #HttpResponseRedirect(reverse_lazy("coupon_details"))

    return render(request, 'coupon_detail.html', context=context)

@login_required
def ManagerView(request):
    if request.user.profile.role!="MR":
        raise PermissionDenied
    return render(request, "manager.html")

@login_required
def TreasurerView(request):
    if request.user.profile.role!="TR":
        raise PermissionDenied
    return render(request, "treasurer.html")