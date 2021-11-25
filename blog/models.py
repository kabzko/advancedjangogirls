from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone

class Post(models.Model):
    """Post fields and functions"""
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def set_publish(self)-> None:
        """Publish unpublish post"""
        self.published_date = timezone.now()
        self.save()

    def get_approved_comments(self)-> QuerySet:
        """Get approved comments"""
        return self.comments.filter(approved_comment=True)
    
    def get_record(self)-> dict:
        """Get record dictionary"""
        try:
            comments = self.get_comments()
            post = {
                "ids": self.id,
                "title": self.title,
                "text": self.text,
                "created_date": self.created_date,
                "published_date": self.published_date,
                "comments_count": len(comments),
                "comments": comments,
            }
            return post
        except Exception as exc: # pragma no cover
            raise exc
        
    def get_comments(self)-> list:
        """Get comments dictionary"""
        try:
            record = [comment.get_record() for comment in self.get_approved_comments()]
            return record
        except Exception as exc: # pragma no cover
            raise exc

    def __str__(self)-> str:
        return self.title
    
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    """Comment fields and functions"""
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def set_approve(self)-> None:
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
        except Exception as exc: # pragma no cover
            raise exc

    def __str__(self)-> str:
        return self.text
