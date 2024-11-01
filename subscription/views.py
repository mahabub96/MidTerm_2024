from django.shortcuts import render
from .models import Subscription
from django.utils import timezone
# Create your views here.

def active_subscriptions(request):
    today = timezone.now().date()
    active_subs = Subscription.objects.filter(start_date__lte=today, end_date__gte=today)

    return render(request, 'active_subscriptions.html', {'active_subs': active_subs})
