from django.conf.urls.defaults import patterns, include, url
from django.conf import settings   
from backupwireless import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home_url'),
    url(r'^switch/$', views.switch, name='switch_url'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'backupwireless/login.html'}, name='login_url'),
    url(r'^accounts/passreset/$', views.PassReset, name='pass_reset_url'),
    url(r'^accounts/logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout_url'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/bmbouter/Documents/Friday/qrlogo/run/static'}),
    )
