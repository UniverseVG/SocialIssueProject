from social_issue.models import SocialIssueLike
from django.http import JsonResponse


def likeApi(request):
    if request.method == "POST":
        issue_id = request.POST["issue_id"]
        user = request.user 
        if user is None or issue_id is None:
            return JsonResponse(status=400,data={"status":"false","message":"Either user id or issueid not available"})

        qs =  SocialIssueLike.objects.filter(user=user,social_issue=issue_id)
        if qs.exists():
            return JsonResponse(status=400,data={"status":"true","message":"You already liked this"})
        like  = SocialIssueLike.objects.create(
            user= user ,
            social_issue_id = issue_id,
        )
        like.save()
        return JsonResponse(status=201,data={"status":"true","message":"Like Added"})
    return JsonResponse(status=400,data={"status":"false","message":"Sorry Get request not allowed"})