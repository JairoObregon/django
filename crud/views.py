
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
 
# relative import of forms
from .models import ESTUDIANTE,CURSOS
from .forms import ESTUDIANTEForm,CURSOSForm

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    formu = ESTUDIANTEForm(request.POST or None)
    print(formu)
    if formu.is_valid():
        formu.save()
        return HttpResponseRedirect("../lista")
    else:
        print(formu)

         
    context["form_e"]= formu
    
    return render(request, "crear_estudiante.html", context)


def create_view_curso(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = CURSOSForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../lista")
    context['form']= form
    
    return render(request, "crear_curso.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = ESTUDIANTE.objects.all()
    context["dataset2"] = CURSOS.objects.all()

    return render(request, "lista.html", context)


# delete view for details
def delete_view_estudiante(request, int):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(ESTUDIANTE, id = int)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("../lista")
 
    return render(request, "delete_view.html", context)


# delete view for details
def delete_view_curso(request, int):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(CURSOS, id = int)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("../lista")
 
    return render(request, "delete_view.html", context)


# update view for details
def update_view_estudiante(request, int):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(ESTUDIANTE, id = int)
 
    # pass the object as instance in form
    form = ESTUDIANTEForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../lista")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view_estudiante.html", context)


# update view for details
def update_view_curso(request, int):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(CURSOS, id = int)
 
    # pass the object as instance in form
    form = CURSOSForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../lista")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view_estudiante.html", context)