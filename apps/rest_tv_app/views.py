from django.shortcuts import render, HttpResponse, redirect
from .models import *
from datetime import datetime
from django.contrib import messages

# Create your views here.

def index(request):

    return redirect('/shows')


def shows(request):

    context = {
        'allShows': Show.objects.all()

    }
    return render(request, 'rest_tv_app/shows.html', context )


def create(request):
    # addedShow = Show.objects.get(id=id)

    return render(request, 'rest_tv_app/index.html')


def creating(request):
    
    errors = Show.objects.basic_validator(request.POST)
    print(errors)

    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')

    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        print(request.POST)

        print(request.POST['date'])

        newShow = Show.objects.create(title=request.POST['title'],
                                    network=request.POST['network'],
                                    date=request.POST['date'],
                                    description=request.POST['description'],
                                    )
        messages.success(request, "Show successfully created")

        context = {
            'allShows': Show.objects.all(),
            'newShow': newShow,
        }

        return redirect('/shows/' + str(newShow.id))


    # newShow = Show.objects.create(title=request.POST['title'],
    #                     network=request.POST['network'],
    #                     date=request.POST['date'],
    #                     description=request.POST['description'],
                        
    #                     )


    # context = {
    #     'allShows': Show.objects.all(),
    #     'newShow': newShow,
    # }

    # return redirect('/shows/' + str(newShow.id))





def showing(request, id):
    show = Show.objects.get(id=id)

    context = {
        'show': Show.objects.get(id=id),
        'id': id
    }

    id = show.id

    return render(request, 'rest_tv_app/show.html', context)


def edit(request, id):
    show = Show.objects.get(id=id)

    context = {
        'show': show,
        'id': id
    }
    
    return render(request, 'rest_tv_app/shows_edit.html', context)


def updating(request, id):

    editedShow = Show.objects.get(id=id)


    errors = Show.objects.basic_validator(request.POST)
    print(errors)


    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/' + str(id) +'/edit')

    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        editedShow.title = request.POST['title']
        editedShow.network = request.POST['network']
        editedShow.date = request.POST['date']
        editedShow.description = request.POST['description']
        editedShow.save() 
        messages.success(request, "Show successfully updated")
        id = editedShow.id
        # redirect to a success route
        return redirect('/' + id)


    # print(editedShow.title)
    # editedShow.title = request.POST['title']
    # editedShow.network = request.POST['network']
    # editedShow.date = request.POST['date']
    # editedShow.description = request.POST['description']
    # editedShow.save() 

    # return redirect('/')

def delete(request, id):
    showToDelete = Show.objects.get(id=id)

    showToDelete.delete()

    return redirect('/shows')
