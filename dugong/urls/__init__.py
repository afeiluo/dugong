from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path, include

from apps.blog.views import BlogListView

# handler500 = "apps.main.views.errors.page_error"
# handler404 = "apps.main.views.errors.not_found"
from apps.photos.views import ImageProcessView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("apps.blog.urls", namespace="blog")),
    path("tutorials/", include("apps.tutorials.urls", namespace="tutorials")),
    path(
        "exchangerates/", include("apps.exchangerates.urls", namespace="exchangerates")
    ),
    path("upload/<int:size>/img/<str:filename>", ImageProcessView.as_view()),
    
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
]

urlpatterns += [path("images/", include("apps.images.urls", namespace="images"))]

urlpatterns += [path("archive/", include("apps.urls.archive", namespace="archive"))]

#
# django allauth url config
# ----------------------------------------------------------------------------------------------------------------------
urlpatterns += [path("account/", include("allauth.urls"))]

#
# search url config
# ----------------------------------------------------------------------------------------------------------------------
urlpatterns += [path("search/", include("apps.search.urls.search", namespace="search"))]

#
# api url config
# ----------------------------------------------------------------------------------------------------------------------
urlpatterns += [path("api/", include("dugong.urls.api", namespace="api"))]

urlpatterns += [re_path(r"^$", BlogListView.as_view(), name="homepage")]

#
# site map config
#
from apps.blog.sitemaps import PostSitemap

sitemaps = {"blog": PostSitemap}

from django.contrib.sitemaps import views
from django.views.decorators.cache import cache_page

urlpatterns += [
    re_path(
        r"^sitemap\.xml$",
        cache_page(86400)(views.sitemap),
        {"sitemaps": sitemaps},
        name="post_sitemaps",
    )
]

from apps.blog.feeds import PostFeeds
from django.contrib.flatpages import views

urlpatterns += [path("feed/posts/", PostFeeds(), name="blog-post-feed")]
urlpatterns += [re_path(r"^pages/(?P<url>.*/?)$", views.flatpage)]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

admin.site.site_header = "jiaxin.im"
admin.site.site_title = "jiaxin.im"
admin.site.index_title = "Welcome to JIAXIN.IM"
