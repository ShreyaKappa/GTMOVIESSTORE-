from django.shortcuts import render, get_object_or_404
from .models import Region, MovieViewCount

def popularity_map(request):
    regions = Region.objects.all()
    return render(request, 'popularity/popularity_map.html', {'regions': regions})

def region_detail(request, region_id):
    region = get_object_or_404(Region, id=region_id)
    trending = MovieViewCount.objects.filter(region=region).order_by('-purchases')[:10]
    return render(request, 'popularity/region_detail.html', {
        'region': region,
        'trending': trending
    })
