from django.shortcuts import render , get_object_or_404
from social_issue.forms import SocialIssueModelForm
from social_issue.models import SocialIssue ,SocialIssueComment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from social_issue.extras import get_filter_queryset
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.db.models import Q

# Create your views here.

@login_required
def index(request):
    if request.method == "POST":
        issueform = SocialIssueModelForm(request.POST)
        if issueform.is_valid():
            issue = issueform.save(commit=False)
            issue.user = request.user 
            issue.save()
            messages.success(request,"Thank You for reporting a issue")

    issueform = SocialIssueModelForm()
    query = request.GET.get("q","")
    issue_filter = request.GET.get("filter") 

    search = False
    if query != "":
        issues = SocialIssue.objects.filter(
            Q(title__icontains=query)|
            Q(description__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)|
            Q(user__username__icontains=query)
        )
        search = True
    else:
        issues = SocialIssue.objects.all().order_by("-submit_date")
    if issue_filter and issue_filter is not "all" :
        issues = get_filter_queryset(issue_filter,issues)



    page = request.GET.get("page",1)
    pagintor = Paginator(issues,2)
    total_count = issues.count()

    try:
        issues = pagintor.page(page)
    except PageNotAnInteger:
        issues = pagintor.page(1)
    except EmptyPage:
        issues = pagintor.page(pagintor.num_pages)
    
    

    context = {
        "form":issueform,
        "issues":issues,
        "search":search,
        "search_count":total_count
    }
    return render(request,"social_issue/index.html",context=context)


def socialIssueDetail(request,pk):
    issue = get_object_or_404(SocialIssue,pk=pk)
    comments = SocialIssueComment.objects.filter(social_issue=issue).order_by("-submit_date")
    if request.method == "POST":
        comment = request.POST["comment"]
        commnet_obj = SocialIssueComment.objects.create(
            comment = comment,
            social_issue = issue,
            user = request.user
        )
        commnet_obj.save()
        messages.success(request,"Thank for your reaction/comment")

    page = request.GET.get("page",1)
    pagintor = Paginator(comments,2)
    try:
        comments = pagintor.page(page)
    except PageNotAnInteger:
        comments = pagintor.page(1)
    except EmptyPage:
        comments = pagintor.page(pagintor.num_pages)
    context = {
        "issue":issue,
        "comments":comments
    }
    return render(request,"social_issue/issue_detail.html",context=context)

