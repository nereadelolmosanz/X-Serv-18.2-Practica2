from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages
from django.views.decorators.csrf import csrf_exempt
import urllib

# Create your views here.



# Declare the form
form = '<form action="" method="POST">'
form += 'Type the url to shorten: <input type="text" name="value">'
form += '<input type="submit" value="Send form"></form><br>'


@csrf_exempt
def main_page(request):
    pages = Pages.objects.all()
    url_list = "<b>Shortened URL | Real URL </b><br>" 
    for page in pages:
        url_list += "<a href='" + page.url + "'>" + str(page.id) + "</a> | " \
             + "<a href='" + page.url + "'>" + page.url + "</a><br>"
      
    if request.method == 'GET':
        response = "<html><body>" + form + url_list + "</body></html>"
        return HttpResponse(response)

    if request.method == 'POST':
        new_url = urllib.unquote(request.body.split('=',1)[1])
        if not new_url.startswith("http") or not newUrl.startswith("https://"):
            new_url = "http://" + new_url

        try:
            Pages.objects.get(url=new_url)
            response = "<html><body><h1>That URL was already saved.</h1>" \
                + form + url_list + "</body></html>"
        except Pages.DoesNotExist:
            new_page = Pages(url=new_url)
            new_page.save()
            response = "<html><body><h1>URL saved successfully!</h1>" + form + url_list \
                + "<a href='" + new_page.url + "'>" + str(new_page.id) + "</a> | " \
                + "<a href='" + new_page.url + "'>" + new_page.url + "</a></body></html>"
        return HttpResponse(response)

    else:
        response = "<html><body><h1>ERROR! Invalid method</h1>" \
            + form + url_list + "</body></html>"
        return HttpResponseNotFound(response)


@csrf_exempt
def get_page(request, resource):
    if request.method == 'GET':
        try:
            page = Pages.objects.get(id=resource)
            response = "<html><head><meta http-equiv='refresh' content='0; url="\
                + page.url +"'></head></html>"
            return HttpResponse(response)
        except Pages.DoesNotExist:
            return HttpResponseNotFound("<h1>NOT FOUND</h1>")

#		try:
#		    resource = int(resource)
#		    if resource in dict_shortenedURL.keys():
#		        url = dict_shortenedURL[resource]
#		        
#		        return HttpResponse(response)
#		    else:
#		        response = "<html><body><h1>The resource is not a shortened URL</h1>" \
#		            + form + urlList + "</body></html>"
#		        return HttpResponseNotFound(response)
#		except ValueError:
#		    response = "<html><body><h1>ERROR! Invalid resource</h1>" \
#		        + form + urlList + "</body></html>"
#		    return HttpResponseNotFound(response)

