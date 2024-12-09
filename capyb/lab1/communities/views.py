from django.shortcuts import render
from .models import Community

def communities_list(request):
    communities = Community.objects.all().order_by('-date')
    return render(request, 'communities/communities_list.html', {'communities': communities})

def community_page(request, slug):
    community = Community.objects.get(slug=slug)
    return render(request, 'communities/community_page.html', {'community': community})




