from django.shortcuts import render
from .models import Profile, SocialLink
from skills.models import Skill
from projects.models import Project, Category


def home(request):
    profile = Profile.objects.first()

    social_links = SocialLink.objects.all()

    skills = Skill.objects.all()

    categories = Category.objects.all()

    projects = (
        Project.objects
        .select_related('category')
        .prefetch_related('images')
        .all()
    )

    context = {
        'profile': profile,
        'social_links': social_links,
        'skills': skills,
        'categories': categories,
        'projects': projects,
    }

    return render(request, 'core/home.html', context)

# Create your views here.
