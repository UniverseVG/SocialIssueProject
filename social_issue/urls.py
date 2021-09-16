from social_issue import views
from django.urls import path
from social_issue.api import likeApi

# all Views/pages url add here

urlpatterns = [
    path('',views.index , name="home" ),
    path('<pk>/detail/',views.socialIssueDetail , name="detail" ),

]
# all api url add here
urlpatterns += [
    path("api/like",likeApi,name="like_api"),
]