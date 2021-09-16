from django import forms
from social_issue.models import SocialIssue

class SocialIssueModelForm(forms.ModelForm):
    

    class Meta:
        model = SocialIssue
        # fields = "__all__"
        fields = ["title","description"]