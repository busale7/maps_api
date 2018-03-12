from django.shortcuts import render
from django.http import JsonResponse 

import requests

# Create your views here.

def homepage(request):
	return render(request, 'home.html')

	
def place_search(request):
	key = "AIzaSyAMo0n6AO7Abth2sE5IJDwpWjXgSK-mG0g"
	query = "Costa"
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key=%s&query=%s&region=kw"%(key,query)

	response = requests.get(url).json()
	context ={
	"response": response ,
	}

	return render(request, 'places.html', context)
	#return JsonResponse(response,safe=False)

def places_search(request):
	key = "AIzaSyAMo0n6AO7Abth2sE5IJDwpWjXgSK-mG0g"
	query = request.GET.get('query',' ')
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key=%s&query=%s&region=kw"%(key,query)

	token =request.GET.get('pt')
	if token:
		url +="&pagetoken=%s"%(token)
	response = requests.get(url).json()
	context ={
	"response": response ,
	}
	#return JsonResponse(response,safe=False)

	return render(request, 'all.html', context)

'''def place_detail(request):
	place_id= request.GET.get('id')
	print(place_id)
	pass'''

def place_detail(request):
    key = "AIzaSyAMo0n6AO7Abth2sE5IJDwpWjXgSK-mG0g"
    map_key="AIzaSyBgGilTUXFkgu9MMPNbC5j_aaVKT743UG0"
    place_id= request.GET.get('id')

    url = "https://maps.googleapis.com/maps/api/place/details/json?key=%s&placeid=%s"%(key,place_id)
    response=requests.get(url).json()
    context= {
    	"response":response,
    	"map":map_key,
    }
    return render(request, 'detail.html', context)
    #return JsonResponse(response,safe=False)


