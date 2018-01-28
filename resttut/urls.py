from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('snippets.urls')),
    url(r'^schema/$', schema_view),

]
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]

