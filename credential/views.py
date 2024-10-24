from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages

from .forms import LuxForm, CadForm, LuxmodelForm
from .models import Cad, Lux, Luxmodel, Interior
from django.http import JsonResponse

def index(request):
    if request.method == "POST":
        form = CadForm(request.POST)
        if form.is_valid():
            form.save()
            # Return a success response (JSON)
            return JsonResponse({'message': 'Form submitted successfully!'}, status=200)
        else:
            # Return form errors if form is invalid
            return JsonResponse({'errors': form.errors}, status=400)

    else:
        form = CadForm()

    main = Lux.objects.all().order_by('-created_at')
    leads = Luxmodel.objects.all().order_by('-created_at')

    context = {
        'main_list': main,
        'lead_list': leads,
        'form': form,
    }
    return render(request, 'index.html', context)







def dashboard(request):
    enquire = Cad.objects.all().order_by('-created_at')
    context = {
        'enquiry_list': enquire
    }
    return render(request,"dashboard.html",context)
def account(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')

        if name == 'caddalladmin' and password == 'caddall@2024':
            return redirect('credential:dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, "cred.html")

def delete(request,taskid):
    task=Cad.objects.get(id=taskid)
    if request.method =='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def main(request):
    if request.method == "POST":
        luximg = request.FILES['luximg']
        luximgs = request.FILES['luximgs']
        luximgss = request.FILES['luximgss']
        lux = Lux(luximg=luximg,luximgs=luximgs,luximgss=luximgss,)
        lux.save()
    return render(request,'main.html')



def updatemain(request):
    main=Lux.objects.all()
    context={'main_list':main}
    return render(request,'updatemain.html',context)
def editlead(request):
    lead=Luxmodel.objects.all()
    context={'lead_list':lead}
    return render(request,'editlead.html',context)

def editmain(request, id):
    main = Lux.objects.get(id=id)
    form = LuxForm(request.POST or None, request.FILES, instance=main)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('credential:updatemain')  # Redirect to wherever you want after successful update
        # If form is not valid, render the edit page with form errors
    return render(request, 'edit3.html', {'form': form, 'main': main})

def uploadlead(request):
    if request.method=="POST":
        photo = request.FILES['photo']
        photo1 = request.FILES['photo1']
        photo2 = request.FILES['photo2']
        photooptional = request.FILES.get('photooptional',None)
        photooptional1 = request.FILES.get('photooptional1',None)
        photooptional2 = request.FILES.get('photooptional2',None)
        luxtitle = request.POST.get('luxtitle',)
        luxloc = request.POST.get('luxloc')
        luxdesc=request.POST.get('luxdesc')
        upload = Luxmodel(photo=photo,photo1=photo1,photo2=photo2,photooptional=photooptional,photooptional1=photooptional1,photooptional2=photooptional2,luxtitle=luxtitle,luxloc=luxloc,luxdesc=luxdesc)
        upload.save()
        return redirect('credential:dashboard')
    return render(request,'uploadlead.html')

def deletelead(request,luxid):
    lead=Luxmodel.objects.get(id=luxid)
    if request.method =='POST':
        lead.delete()
        return redirect('/')
    return render(request,'delete.html')

def updatelead(request,lexid):
    lex = Luxmodel.objects.get(id=lexid)
    form = LuxmodelForm(request.POST or None, request.FILES, instance=lex)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('credential:editlead')  # Redirect to wherever you want after successful update
        # If form is not valid, render the edit page with form errors
    return render(request, 'edit4.html', {'form': form, 'lex': lex})

def viewinterior(request):
    internal=Interior.objects.all().order_by('-created_at')
    context={'interior_list':internal}
    return render(request,'interior.html',context)
def uploadinterior(request):
    if request.method == "POST":
        interior=request.FILES['interior']
        int=Interior(interior=interior)
        int.save()
        return redirect('credential:dashboard')
    return render(request,"uploadinterior.html")
def deleteinterior(request,interid):
    dsgn=Interior.objects.get(id=interid)
    if request.method =='POST':
        dsgn.delete()
        return redirect('/')
    return render(request,'delete.html')
def editinterior(request):
    internal = Interior.objects.all().order_by('-created_at')
    context = {'interior_list': internal}
    return render(request, 'editinterior.html', context)


def about(request):
    return render(request,"about.html",)


def demo(request):
    if request.method == "POST":
        form = CadForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return HttpResponseRedirect('/')
    else:
        form = CadForm()

    return render(request, 'demo.html',)