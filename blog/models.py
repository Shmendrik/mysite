from django.db import models

# Create your models here.

import datetime

#our blog
class Post(models.Model):
	# title post
    title = models.CharField(max_length=60)
    # body post
    text = models.TextField()
    # publication date
    pub_date = models.DateTimeField('date published')

    def announcer(self):
        #for announce in post loads
        num = 300
        try:
            num = self.text[:num].rindex(u'.')
        except: num = (len(self.text) if len(self.text) < num else num)
        return self.text[:num+1]

    def __unicode__(self):
        return self.title

#our blog comments
class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment_author = models.CharField(max_length=60)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
  	
    def __unicode__(self):
        return self.post
