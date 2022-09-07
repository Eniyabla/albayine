from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from home.models import Media, Skill, Education, userprofile, Portfolio, Category, About, Experience, Images,ContactMessage, Message


# Create your views here.
def index(request):
    about = About.objects.get(pk=1)
    profile = userprofile.objects.get(pk=1)
    medias = Media.objects.filter(status=True)
    skills = Skill.objects.filter(status=True)
    categories = Category.objects.filter(status=True)
    portfolios = Portfolio.objects.filter(status=True)
    educations = Education.objects.filter(status=True).order_by('-end')[:3]
    experience = Experience.objects.filter(status=True).order_by('-end')[:3]
    context = {
        'medias': medias,
        'skills': skills,
        'educations': educations,
        'profile': profile,
        'portfolios': portfolios,
        'categories': categories,
        'about': about,
        'experience': experience,

    }
    return render(request, 'index.html', context)


def portfoliodetail(request, id):
    project = Portfolio.objects.get(id=id)
    images = Images.objects.filter(portfolio_id=id)[:2]
    context = {
        'project': project,
        'images': images,
    }
    return render(request, 'portfoliodetail.html', context)


def contactMe(request):
    if request.method == 'POST':
        form = ContactMessage
        data = Message()
        if form.is_valid:
            data.subject = request.POST['subject']
            data.name = request.POST['name']
            data.email = request.POST['email']
            data.message = request.POST['message']
            data.status = False
            data.save()
            message='Your message has been sent. Thank you!'
            context={
                'message':message,
            }
    return HttpResponseRedirect(reverse('home_index'),context)
