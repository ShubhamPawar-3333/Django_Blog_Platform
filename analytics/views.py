# analytics/views.py
from django.shortcuts import render
from blog_app.models import BlogPost
from .models import PageView
from django.db.models import Count

def analytics_dashboard(request):
    total_views = PageView.objects.count()
    unique_visitors = PageView.objects.values('ip_address').distinct().count()
    popular_posts = (BlogPost.objects
                     .annotate(view_count=Count('views'))
                     .order_by('-view_count')[:5])  # Top 5 most viewed posts
    return render(request, 'analytics/dashboard.html', {
        'total_views': total_views,
        'unique_visitors': unique_visitors,
        'popular_posts': popular_posts,
    })