from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image



def welcome(request):
    return render(request, 'welcome.html')



def photo_today(request):
    images = Image.objects.all()
    return render(request, 'all-photo/today-photo.html', {"images": images})



def past_days_photo(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photo_of_day)

    return render(request, 'all-photo/past-photo.html', {"date": date})


def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = IMage.search_by_image_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photo/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photo/search.html',{"message":message})