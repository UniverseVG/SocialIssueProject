from django.db import models

# Create your models here.


from django.contrib.auth import get_user_model

User = get_user_model()


class SocialIssue(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description =  models.TextField()
    submit_date = models.DateTimeField("Date/Time Submited",auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_likes(self):
        return self.likes.count()

    def get_comments(self):
        return self.comments.count()


    def __str__(self):
        return "%s : %s" %(self.user.username,self.title)

class SocialIssueComment(models.Model):
    comment  = models.TextField()
    submit_date = models.DateTimeField("Date/Time Commented",auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    social_issue = models.ForeignKey(SocialIssue, on_delete=models.CASCADE,related_name="comments")

class SocialIssueLike(models.Model):
    # create_at
    timestamp = models.DateTimeField("Date/Time Liked",auto_now_add=True) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    social_issue = models.ForeignKey(SocialIssue, on_delete=models.CASCADE,related_name="likes")