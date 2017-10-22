from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import (
   password_reset,
   password_reset_done,
   password_reset_confirm,
   password_reset_complete
)

urlpatterns = [
    url(r'^', include('{{ project_name}}_app.urls')),
    url(r'^accounts/password/reset/$',
        password_reset,
        {'template_name':
        'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name':
        'registration/password_reset_done.html'},
        name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'template_name':
        'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$',
        password_reset_complete,
        {'template_name':
        'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
]
