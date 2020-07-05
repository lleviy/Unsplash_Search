from django.shortcuts import render

from django.http import JsonResponse

from .api import unsplash_api
from unsplash.errors import UnsplashError


def search_photos(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        page = request.GET.get('page')
        results_per_page = 9
        photos_url = []
        try:
            search = unsplash_api.search.photos(page=page, per_page=results_per_page, query=q)
        except UnsplashError:
            return render(request, '', {})
        else:
            for photo in search['results']:
                photos_url.append(f'https://source.unsplash.com/{photo.id}/1600x900')
        return JsonResponse({'photos_url': photos_url}, safe=False)
    return JsonResponse({},safe=False)


def get_random_photos(count=9, collection='983862'):
    '''Random generation of Unsplash photos from a specific collection'''
    photos_url = []
    search = unsplash_api.photo.random(orientation='landscape', count=count, collections=collection)
    for photo in search:
        photos_url.append(f'https://source.unsplash.com/{photo.id}/1600x900')
    return photos_url
