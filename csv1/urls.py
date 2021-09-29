from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from csvfile.views import profile_upload,singleVendor,display, singleVendor2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profile_upload, name="profile_upload"),
    path('display', display, name="display"),
    path('detail<int:id>/', singleVendor, name='detail'), # 這一行
    path('modify<int:id>/', singleVendor2, name='modify'), # 這一行
]