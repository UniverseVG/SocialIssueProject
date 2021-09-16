from datetime import timedelta, datetime
def get_filter_queryset(issue_filter,issues_queryset):
    # if issue_filter == "all":
    #     issues_queryset = 
    if issue_filter == "trending":
        # trending is the issue like in last 
        issues_queryset = issues_queryset.filter(
            # query for last 30 days
            submit_date__gt = datetime.today() - timedelta(days=30),
            # likes greater than 2
            likes__gt =2
        ).distinct()
    if issue_filter == "recent":
        # recnet => last 30 days
        issues_queryset = issues_queryset.filter(
            # query for last 30 days
            submit_date__gt = datetime.today() - timedelta(days=30)
        ).distinct()
    if issue_filter == "most-discussed":
        # most-discussed : has most comments 
        issues_queryset = issues_queryset.filter(
            # comments greater than 2
                       comments__gt =2
        ).distinct()
        
    return issues_queryset