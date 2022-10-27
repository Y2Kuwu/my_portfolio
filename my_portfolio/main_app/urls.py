from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/contact_index/', views.contact_index, name='contact_index'),
    path('reviews/review_index/', views.review_index, name='review_index'),
    path('link_page/links', views.link, name='link_page'),
    path('contact/create_contact/', views.create_contact, name= 'create_contact'),
    path('reviews/create_review/', views.create_review, name= 'create_review'),
]