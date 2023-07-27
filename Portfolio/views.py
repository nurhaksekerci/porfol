from django.shortcuts import render, redirect
from .models import *
from .models import ContactForm
def index(request):
    # Fetch all gallery items from the database
    gallery_items = GalleryItem.objects.all()
    testimonials = Testimonial.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Create and save the ContactMessage object
        contact_message = ContactForm(name=name, email=email, phone=phone, message=message)
        contact_message.save()

        # Redirect to a success page or render the same page with a success message
        return redirect('index')  # Replace 'success_page' with the URL name of your success page

    return render(request, 'Portfolio/index.html', {'gallery_items': gallery_items, 'testimonials' : testimonials})
