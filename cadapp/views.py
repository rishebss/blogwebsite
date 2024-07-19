from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache

from . models import Complete
from . models import Incomplete
from . forms import AddcompleteForm
from . forms import AddIncompleteForm

# Create your views here.
def complete(request):
    completed = Complete.objects.all().order_by('-created_at')
    context = {
        'completed_list': completed
    }
    return render(request, 'grid.html', context)


def addcomplete(request):
    if request.method == "POST":
        pic = request.FILES['pic']
        title = request.POST.get('title')
        location = request.POST.get('location')

        photos = request.FILES.getlist('photos')
        if len(photos) > 6:
            return render(request, 'addcomplete.html', {'error': 'You can upload up to 6 images only.'})

        photo = photos[0] if len(photos) > 0 else None
        photo1 = photos[1] if len(photos) > 1 else None
        photo2 = photos[2] if len(photos) > 2 else None
        photooptional = photos[3] if len(photos) > 3 else None
        photooptional1 = photos[4] if len(photos) > 4 else None
        photooptional2 = photos[5] if len(photos) > 5 else None

        completeproject = Complete(
            pic=pic,
            title=title,
            location=location,
            photo=photo,
            photo1=photo1,
            photo2=photo2,
            photooptional=photooptional,
            photooptional1=photooptional1,
            photooptional2=photooptional2
        )
        completeproject.save()
        return redirect('credential:dashboard')
    return render(request, 'addcomplete.html')

def addincomplete(request):
    if request.method == "POST":
        picture = request.FILES['picture']
        heading = request.POST.get('heading')
        place = request.POST.get('place')

        photos = request.FILES.getlist('photos')
        if len(photos) > 6:
            return render(request, 'addincomplete.html', {'error': 'You can upload up to 6 images only.'})

        photo = photos[0] if len(photos) > 0 else None
        photo1 = photos[1] if len(photos) > 1 else None
        photo2 = photos[2] if len(photos) > 2 else None
        photooptional = photos[3] if len(photos) > 3 else None
        photooptional1 = photos[4] if len(photos) > 4 else None
        photooptional2 = photos[5] if len(photos) > 5 else None

        incompleteproject = Incomplete(
            picture=picture,
            heading=heading,
            place=place,
            photo=photo,
            photo1=photo1,
            photo2=photo2,
            photooptional=photooptional,
            photooptional1=photooptional1,
            photooptional2=photooptional2
        )
        incompleteproject.save()
        return redirect('credential:dashboard')
    return render(request, 'addincomplete.html')
def incomplete(request):
    ongoing=Incomplete.objects.all().order_by('-created_at')
    context={'ongoing_list':ongoing}
    return render(request,'incomplete.html',context)
def viewcomplete(request):
    complete=Complete.objects.all().order_by('-created_at')
    context={'completed_list':complete}
    return render(request,'editcomplete.html',context)

def deletecomplete(request,completeid):
    complete=Complete.objects.get(id=completeid)
    if request.method =='POST':
        complete.delete()
        return redirect('/')
    return render(request,'delete.html')

def viewincomplete(request):
    incomplete=Incomplete.objects.all().order_by('-created_at')
    context={'incompleted_list':incomplete}
    return render(request,'editincomplete.html',context)

def deleteincomplete(request,incompleteid):
    incomplete=Incomplete.objects.get(id=incompleteid)
    if request.method =='POST':
        incomplete.delete()
        return redirect('/')
    return render(request,'delete.html')


@never_cache
def updatecomplete(request, id):
    complete = Complete.objects.get(id=id)
    form = AddcompleteForm(request.POST or None, request.FILES, instance=complete)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cadapp:viewcomplete')  # Redirect to wherever you want after successful update
        # If form is not valid, render the edit page with form errors
    return render(request, 'edit.html', {'form': form, 'complete': complete})
def updateincomplete(request, id):
    incomplete = Incomplete.objects.get(id=id)
    form = AddIncompleteForm(request.POST or None, request.FILES, instance=incomplete)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cadapp:viewincomplete')  # Redirect to wherever you want after successful update
        # If form is not valid, render the edit page with form errors
    return render(request, 'edit2.html', {'form': form, 'incomplete': incomplete})

