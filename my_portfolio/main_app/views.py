from django.shortcuts import render, redirect
from .models import Review, Contact
from django.contrib.auth.decorators import user_passes_test
from .forms import ReviewForm, ContactForm



sub_review = False
all_reviews = []

def home(request):
    return render(request, "home.html/")

def link(request):
    return render(request, "link_page/links.html", {})

@user_passes_test(lambda u: u.is_superuser)
def contact_index(request):
        contacts = Contact.objects.all()
        return render(request, "contact/contact_index.html/", {'contacts':contacts})
    

def review_index(request):
    reviews = Review.objects.all()
    return render(request, "reviews/review_index.html", {'reviews':reviews})

def create_review(request):
    if request.method == "POST":
        rev_form = ReviewForm(request.POST)
        if rev_form.is_valid():
            rev_form.save()
            return redirect('home')
    else: 
        rev_form = ReviewForm()
        return render(request, 'reviews/create_review.html/', {"rev_form":rev_form})

def create_contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('home')
    else: 
        contact_form = ContactForm()
        return render(request, 'contact/create_contact.html/', {"contact_form":contact_form})

