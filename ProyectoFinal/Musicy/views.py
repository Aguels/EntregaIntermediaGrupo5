from django.shortcuts import render
from django.template import loader, context
from django.http import HttpResponse
from Musicy import forms as f
import Musicy.models as mod
from django.shortcuts import redirect
import django.views.generic as dv



def home(request):
    dict = {}
    plantilla = loader.get_template("Home.html")
    doc = plantilla.render(dict)
    return HttpResponse(doc)

def test(request):
    dict = {}
    plantilla = loader.get_template("Pater.html")
    doc = plantilla.render(dict)
    return HttpResponse(doc)

def blog(request):
    dict = {}
    plantilla = loader.get_template("Blog.html")
    doc = plantilla.render(dict)
    return HttpResponse(doc)

def cancionero(request):
    dict = {}
    plantilla = loader.get_template("Cancionero.html")
    doc = plantilla.render(dict)
    return HttpResponse(doc)

def registro(request):
    dict = {}
    plantilla = loader.get_template("Registro.html")
    doc = plantilla.render(dict)
    return HttpResponse(doc)

def navegador(request):

    return render(request, "Navegador.html")

def rehome(request):
    response = redirect('/musicy/home/')
    return response

def formulario(request):
    if request.method == "POST":
        Form = f.mus(request.POST)
        print(Form)
        if Form.is_valid:
            dato = Form.cleaned_data
            Up = mod.Musician(nombre=dato["Nombre"], rol=dato["Rol"])
            Up.save()

            return redirect("/musicy/musicos/")
    
    else:
        Form = f.mus()
    
    return render(request, "Forms.html", {"Form":Form})

def buscarmus(request):
    if request.GET["Rol"]:
        rol = request.GET["Rol"]
        ret = mod.Musician.objects.filter(rol__icontains=rol)
        return render(request, "Resultado.html", {"ret":ret, "rol": rol})

    else:
        respuesta = "No enviaste datos."
        return HttpResponse(respuesta)

def show(request):
    musicos = mod.Musician.objects.all()
    return render(request, "Listado.html", {"Músicos":musicos})

def deletemus(request, id):
    musico = mod.Musician.objects.get(id=id)
    musico.delete()
    return redirect("/musicy/musicos/listado/")

def editmus(request,id):
    musico = mod.Musician.objects.get(id=id)
    if request.method == "POST":
        Formed = f.mus(request.POST)
        print(Formed)

        if Formed.is_valid:
            datos = Formed.cleaned_data
            musico.nombre = datos["Nombre"]
            musico.rol = datos["Rol"]
            musico.save()
            return redirect("/musicy/musicos/listado/")
    else:
        Formed = f.mus(initial= {"Nombre" : musico.nombre, "Rol" : musico.rol})
    return render(request, "EditarMusico.html",{"Formed":Formed,"id":id})

class blog(dv.ListView):
    model = mod.BlogEntry
    template_name = "Blog.html"

class blogdetalle(dv.DetailView):
    model = mod.BlogEntry
    template_name = "BlogDetalle.html"

class crearblog(dv.CreateView):
    model = mod.BlogEntry
    success_url = "musicy/blog/"
    fields = ["titulo","cuerpo"]

class editarblog(dv.UpdateView):
    model = mod.BlogEntry
    success_url = "musicy/blog/"
    fields = ["titulo","cuerpo"]
    template_name = "BlogForm.html"

class eliminarblog(dv.DeleteView):
    model = mod.BlogEntry
    success_url = "musicy/blog/"
    template_name = "BlogDelete.html"    