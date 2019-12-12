from django.conf.urls import url

from apps.blog.views import (
    BlogListView,
    BlogDetailView,
    PostTagListView,
    # BlogYearArchiveView,
)

app_name = "blog"

urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='list'),
    # url(r'^(?P<year>[0-9]{4})/$',
    #     BlogYearArchiveView.as_view(), name="year_archive"),

    url(r'^tags/(?P<tid>\d+/?$)', PostTagListView.as_view(), name='tags'),
    url(r'^(?P<slug>[\w|\-]+)/?$', BlogDetailView.as_view(), name='detail'),
]
