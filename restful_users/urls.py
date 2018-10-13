from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.login_reg.urls', namespace='login_reg')),
    url(r'^users', include('apps.users.urls', namespace='users'))
]
