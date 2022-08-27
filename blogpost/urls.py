from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from posts.views import homepage, post, about, search, postlist, allposts
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'homepage'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about,name = 'about'),
    path('search/', search, name = 'search'),
    path('postlist/<slug>', postlist, name = 'postlist'),
    path('post/', allposts, name = 'allposts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)