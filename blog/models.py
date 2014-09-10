from django.db import models

# Create your models here.

import datetime

class Post(models.Model):
	# title post
    title = models.CharField(max_length=60)
    # body post
    text = models.TextField()
    # publication date
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title
