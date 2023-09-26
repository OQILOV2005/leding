from django.shortcuts import render,redirect
from.models import *
def index_view(request):
    context = {
        'Banner': Banner.objects.last(),
        'About': About.objects.last(),
        'Speakers': Speakers.objects.all().order_by('-id')[:6],
        'Sponsor': Sponsor.objects.all().order_by('-id')[:8],
        'Venue': Venue.objects.all().order_by('-id')[:8],
        'Hotel': Hotel.objects.all().order_by('-id')[:3],
        'Ticet': Ticet.objects.all(),
        'Faq':Faq.objects.all().order_by('-id')[:6],
    }
    return render(request,'index.html',context)


def create_contact_view(request):
   if request.method == "POST":
      name = request.POST['name']
      email = request.POST['email']
      message = request.POST['message']
      Contact.objects.create(
         name=name,
         email=email,
         message=message,
      )
      return redirect('index_url')
   context = {
       'Banner': Banner.objects.last(),
       'About': About.objects.last(),
       'Speakers': Speakers.objects.all().order_by('-id')[:6],
       'Sponsor': Sponsor.objects.all().order_by('-id')[:8],
       'Venue': Venue.objects.all().order_by('-id')[:8],
       'Gallery': Gallery.objects.all().order_by('-id')[:8],
       'Hotel': Hotel.objects.all().order_by('-id')[:3],
       'Ticet': Ticet.objects.all().order_by('-id')[:3],
       'Faq': Faq.objects.all().order_by('-id')[:6],
   }
   return render(request, 'index.html', context)
