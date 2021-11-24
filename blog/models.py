from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def get_record(self)-> dict:
        """Get record dictionary"""
        try:
            comments = self.get_comments()
            post = {
                "id": self.id,
                "title": self.title,
                "text": self.text,
                "created_date": self.created_date,
                "published_date": self.published_date,
                "comments_count": len(comments),
                "comments": comments,
            }
            return post
        except Exception as exc:
            raise exc
        
    def get_comments(self)-> list:
        """Get comments dictionary"""
        try:
            record = [comment.get_record() for comment in self.approved_comments()]
            return record
        except Exception as exc:
            raise exc

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
        
    def get_record(self)-> dict:
        """Get record dictionary"""
        try:
            comment = {
                "id": self.id,
                "post": self.post.id,
                "text": self.text,
                "created_date": self.created_date,
                "approved_comment": self.approved_comment,
            }
            return comment
        except Exception as exc:
            raise exc

    def __str__(self):
        return self.text
