from subprocess import Popen
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from backupwireless.models import AccessPoint, WirelessNetwork

class HomeView(TemplateView):
    
    template_name = "backupwireless/home.html"
    
    def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		online = WirelessNetwork.objects.all()[0].online
		context.update({"statusText": 'Enabled' if online else 'Disabled'})
		context.update({"buttonText": 'Disable' if online else 'Enable'})
		unreachableHosts = self.request.session.get('unreachable_hosts')
		if unreachableHosts:
			unreachableHosts = unreachableHosts.strip().rstrip(',')
		else:
			unreachableHosts = "start"
		context.update({"unreachableHosts": unreachableHosts})
		return context
        
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

@login_required
def switch(request):
	unreachable_hosts = ""	
	if WirelessNetwork.objects.all()[0].online:
		for ap in AccessPoint.objects.all():
			pHandle = Popen(['ssh', '-o ConnectTimeout=1', ap.username + '@' + ap.ip, 'nvram', 'set', 'ath0_net_mode=disabled']) 
			exitCode = pHandle.wait()
			if exitCode != 0:
					unreachable_hosts += ap.ip + ","
					continue
			pHandle = Popen(['ssh', '-o ConnectTimeout=1', ap.username + '@' + ap.ip, 'nvram', 'commit']) 
			exitCode = pHandle.wait()		
			pHandle = Popen(['ssh', '-o ConnectTimeout=1', ap.username + '@' + ap.ip, 'reboot']) 
			exitCode = pHandle.wait()
		WirelessNetwork.objects.all().update(online=0)
	else:
		for ap in AccessPoint.objects.all():
			pHandle = Popen(['ssh', '-o ConnectTimeout=1', ap.username + '@' + ap.ip, 'nvram', 'set', 'ath0_net_mode=mixed']) 
			exitCode = pHandle.wait()
			if exitCode != 0:
					unreachable_hosts += ap.ip + ","
					continue
			pHandle = Popen(['ssh', '-o ConnectTimeout=1',ap.username + '@' + ap.ip, 'nvram', 'commit']) 
			exitCode = pHandle.wait()
			pHandle = Popen(['ssh', '-o ConnectTimeout=1', ap.username + '@' + ap.ip, 'reboot']) 
			exitCode = pHandle.wait()
		WirelessNetwork.objects.all().update(online=1)
	
	if not unreachable_hosts:
		request.session['unreachable_hosts'] = unreachable_hosts
	else:
		request.session['unreachable_hosts'] = "none"

	return HttpResponseRedirect("/")

@login_required
def PassReset(request):
    if request.method == "GET":
        return render_to_response("backupwireless/passreset.html", {}, context_instance=RequestContext(request))
    else:
        user = request.user
        current_pass = request.POST.get("current")
        new_pass1 = request.POST.get("new1")
        new_pass2 = request.POST.get("new2")
        context = {"success": False, "current_error": False, "new_error": False}

        if user.check_password(current_pass):
            if new_pass1 == new_pass2:
                user.set_password(new_pass1)
                user.save()
                context["success"] = True
            else:
                context["new_error"] = True
        else:
            context["current_error"] = True

        return render_to_response("backupwireless/passreset.html", context, context_instance=RequestContext(request))
