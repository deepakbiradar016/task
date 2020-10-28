from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from accounts.views import upload_file, record_list, RecordList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="home.html")),
    path('accounts/upload-file/', upload_file, name="upload_file"),
    path('accounts/record-list/', record_list, name="record_list"),
    path('accounts/record-list2/', RecordList.as_view(), name="record_list2")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
