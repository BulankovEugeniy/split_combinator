from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Channels
from django.views.decorators.csrf import csrf_exempt
from . modules.parse_data import parse
from . modules.make_mixes import generate_mix
import os
import mimetypes
from wsgiref.util import FileWrapper




@csrf_exempt
def index(request):
	result = ""
	context = { 
		'input_channels': Channels.objects.all()
	}
	if request.method == "POST":
		req = parse(request.read())
		#print(req)
		channels_to_calculation = []
		distr_to_calculation = []
		for obj in Channels.objects.all():
			channels_to_calculation.append(obj.channel)
			if obj.distr == "National\t":
				distr_to_calculation.append("National")
			else:
				distr_to_calculation.append(obj.distr)
		mixes_list = generate_mix(req, channels_to_calculation, distr_to_calculation)
		result = HttpResponse(mixes_list)
	else:
		result = render(request, 'get_naturals/index.html', context)
	return result
