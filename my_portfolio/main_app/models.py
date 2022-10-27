
from django.db import models
from django.contrib.postgres.fields import ArrayField

STARS = (
    ('1', 'one'),
    ('2', 'two'),
    ('3', 'three'),
    ('4', 'four'),
    ('5', 'five'),
)

# class ReviewList(models.Model):
#     review_list = ArrayField(
#     ArrayField(
#         models.CharField(max_length =1000)
#     )    
#     )
#     def __str__(self):
#         return self.review_list


class Review(models.Model):
    stars = models.CharField(
    max_length = 5,
    choices=STARS,
    default = [4][0]
    )
    comment = models.TextField(max_length=300)
    alias = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.alias , self.stars, self.comment}"  #just name and rating click to see comment

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=11)
    buisness = models.CharField(max_length=300)
    title = models.CharField(max_length=300)

    def __str__(self):    
        return f"{self.name, self.email, self.phone , self.buisness, self.title}"

