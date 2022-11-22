from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import Setting,Contact
from apps.hotels.models import Hotels

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    hotels =  Hotels.objects.all()
    context = {
        'setting' : setting,
        'hotels' : hotels,
    }
    return render(request, 'booking/index.html', context)

def thank_you(request):
    return render (request, 'booking/thank_u.html')

def contact(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact.objects.create(name = name, email = email, message = message,)
        send_mail(
                    # title:
                    f"{setting.title}",
                    # message:
                    f"{name} спасибо за ваше сообщение. В скором времени мы вам ответим. Ваше сообщение: {message}",
                    # from:
                    "noreply@somehost.local",
                    # to:
                    [email]
            )
        return redirect('thank_you')
    context = {
        'setting' : setting
    }
    return render (request, 'booking/contact.html', context)