from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from .forms import BaseModeForm
from .models import BaseModule, BaseMode, Intermediate, IntermediateMode
from datetime import datetime

# Create your views here.

def index(request):

	return render(request, 'index.html', {})

@csrf_protect
def validcrn(request):
	#crn = get_object_or_404(BaseModule, pk=pk)

	if request.method == 'POST':
		email = request.POST['email']
		teaching = request.POST['teaching']
		mode = request.POST['response']

		if teaching == 'NAS':
			data = BaseModule.objects.filter(email=email).values()
			
			if not data:
				message = 'Email Not Found. Contact Us.'
				return render(request, 'index.html', {'message':message})
			else:
				for user in data:
					fk = user['id']
					user_email = user['email']

				
				#check if user exist
				user = BaseMode.objects.filter(base_id = fk).exists()
				user_mode = BaseMode.objects.filter(base_id = fk).values()
				user_base = BaseModule.objects.filter(id=fk).values()
				if user: #if user exist,
					for user in user_mode:
						modeuser = user['response']

					if modeuser == 'remote': #check what user selected
						link= 'https://drive.google.com/file/d/17aTj2ffSx4WXGqAjudxfKNTwd3qsIefj/view?usp=sharing_eil_m&ts=634019ec'
					else: #if onsite
						link = 'https://drive.google.com/file/d/1u_nR39hRMb-qLwKtHLHW2N7R__pFsjc3/view?usp=sharing_eip_m&ts=634019b3'

					existmessage = f'Sorry, Mode cannot be changed. Mode selected was {modeuser.upper()}'
					context = {'data' : user_base, 'existmessage':existmessage, 'link':link}
					return render(request, 'validcrn.html', context)

				else:
					form = BaseMode(base_id=fk, response = request.POST.get('response'), response_date = datetime.now())
					form.save()

				if mode == 'remote':
					remotelink= 'https://drive.google.com/file/d/17aTj2ffSx4WXGqAjudxfKNTwd3qsIefj/view?usp=sharing_eil_m&ts=634019ec'
					message = 'remote'
					context = {'data' : data, 'message':message, 'link':remotelink}
				else:
					onsitelink = 'https://drive.google.com/file/d/1u_nR39hRMb-qLwKtHLHW2N7R__pFsjc3/view?usp=sharing_eip_m&ts=634019b3'
					message = 'onsite'
					context = {'data' : data, 'message':message, 'link':onsitelink}
				
				#context = {'data' : data, 'message':message, 'link':link}

				#return HttpResponseRedirect(reverse('validcrn'))
				return render(request, 'validcrn.html', context)
		else:
			data = Intermediate.objects.filter(email=email).values()

			if not data:
				message = 'Email Not Found. Contact Us.'
				return render(request, 'index.html', {'message':message})

			for user in data:
				fk = user['id']

			#check if user exist
			intuser = IntermediateMode.objects.filter(int_id = fk).exists()
			user_mode = IntermediateMode.objects.filter(int_id = fk).values()
			user_int = Intermediate.objects.filter(id=fk).values()

			if intuser: #if user exist,
				for user in user_mode:
					modeuser = user['response']

				if modeuser == 'remote': #check what user selected
					mode = 'remote'
					remotelink= 'https://drive.google.com/file/d/1RxX6VMDZMsdaXcD0sPdBwKqgRELOspYG/view?usp=sharing_eil_m&ts=63401a62'
					existmessage = f'Sorry, Mode cannot be changed. Mode selected was {mode.upper()}'
					context = {'data' : user_int, 'existmessage':existmessage, 'link':remotelink}
				else: #if onsite
					mode = 'onsite'
					existmessage = f'Sorry, Mode cannot be changed. Mode selected was {mode.upper()}'
					onsitelink= 'https://drive.google.com/file/d/1HxV4c3UcKPBIPBkIyB9Qgn0qENIVcsDu/view?usp=sharing_eil_m&ts=63401a24'
					context = {'data' : user_int, 'existmessage':existmessage, 'link':onsitelink}

				return render(request, 'validcrn.html', context)

			else:
				form = IntermediateMode(int_id=fk, response = request.POST.get('response'), response_date = datetime.now())
				form.save()
				
			if mode == 'remote':
				remotelink= 'https://drive.google.com/file/d/1RxX6VMDZMsdaXcD0sPdBwKqgRELOspYG/view?usp=sharing_eil_m&ts=63401a62'
				message = 'remote'
				context = {'data' : data, 'message':message, 'link':remotelink}
			else:
				onsitelink = 'https://drive.google.com/file/d/1HxV4c3UcKPBIPBkIyB9Qgn0qENIVcsDu/view?usp=sharing_eil_m&ts=63401a24'
				message = 'onsite'
				context = {'data' : data, 'message':message, 'link':onsitelink}
			 
			
			#context = {'data' : data, 'message':message, 'link':link}

			#return HttpResponseRedirect(reverse('validcrn'))
			return render(request, 'validcrn.html', context)
	else:
		message = 'Email Not Found. Contact Us.'
		return render(request, 'index.html', {'message':message})
		


