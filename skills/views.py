from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Skill

# Create your views here.


def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'skills/skill_list.html', {
        'skills': skills
    })


def skill_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        category = request.POST.get('category', '')
        level = request.POST.get('level', 50)
        icon = request.POST.get('icon', '').strip()

        if name and category:
            Skill.objects.create(
                name=name,
                category=category,
                level=level,
                icon=icon
            )
            return redirect('skill_list')

    return render(request, 'skills/skill_form.html', {
        'skill': None,
        'categories': Skill.CATEGORY_CHOICES
    })


def skill_update(request, pk):
    skill = get_object_or_404(Skill, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        category = request.POST.get('category', '')
        level = request.POST.get('level', 50)
        icon = request.POST.get('icon', '').strip()

        if name and category:
            skill.name = name
            skill.category = category
            skill.level = level
            skill.icon = icon
            skill.save()
            return redirect('skill_list')

    return render(request, 'skills/skill_form.html', {
        'skill': skill
    })


def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)

    if request.method == 'POST':
        skill.delete()
        return redirect('skill_list')

    return render(request, 'skills/skill_confirm_delete.html', {
        'skill': skill
    })

