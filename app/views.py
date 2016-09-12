from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver

import random

from app.models import Person, Task, Assignment
from app.forms import AssignmentForm


@receiver(post_save, sender=Person)
def my_handler(sender, **kwargs):
    person = Person.objects.latest('addeddate')
    tasks = Task.objects.all()
    for task in tasks:
        obj, created = Assignment.objects.get_or_create(person=person, task=task)


def index(request):
    people = Person.objects.order_by('-addeddate')
    return render(request, 'app/index.html',
        {'people': people})


@require_http_methods(["GET", "POST"])
def profile(request, shortname=None):
    people = Person.objects.order_by('-addeddate')
    person = get_object_or_404(Person, shortname=shortname)
    assignments = Assignment.objects.filter(person=person)
    randimg = random.randint(1, 20)
    form = AssignmentForm(request.POST or None)

    if request.method == "POST":
        check_values = request.POST.getlist('assignment')

        for check in check_values:
            task = Assignment.objects.get(id=check)
            task.complete = True
            task.save()
            messages.success(request, 'Task(s) marked complete')

    context = {'shortname': shortname,
                'people': people,
                'person': person,
                'assignments': assignments,
                'form': form,
                'message': messages,
                'randimg': randimg}

    return render(request, 'app/profile.html', context)
