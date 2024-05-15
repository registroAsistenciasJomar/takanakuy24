from django.shortcuts import render, redirect
from gestorResultados.models import Canto, Baile, PlayBack, Conocimientos, Juegos, Barras

# Create your views here.
def ingresar_canto(request):

    if request.method=="POST":
        grado = request.POST.get('grado')
        seccion = request.POST.get('seccion')
        jurado = request.POST.get('jurado')
        crit_01 = request.POST.get('crit01')
        crit_02 = request.POST.get('crit02')
        crit_03 = request.POST.get('crit03')
        crit_04 = request.POST.get('crit04')
        calificacion = int(crit_01)+int(crit_02)+int(crit_03)+int(crit_04)

        Canto.objects.create(jurado=jurado, grado= grado, seccion=seccion, criterio_1=crit_01,
                             criterio_2=crit_02, criterio_3=crit_03, criterio_4=crit_04,
                             calificacion=calificacion)
        
        return redirect("/envio_exitoso/")

    return render(request ,"ingresar_canto.html")

def ingresar_baile(request):

    if request.method=="POST":
        grado = request.POST.get('grado')
        seccion = request.POST.get('seccion')
        jurado = request.POST.get('jurado')
        crit_01 = request.POST.get('crit01')
        crit_02 = request.POST.get('crit02')
        crit_03 = request.POST.get('crit03')
        crit_04 = request.POST.get('crit04')
        calificacion = int(crit_01)+int(crit_02)+int(crit_03)+int(crit_04)

        Baile.objects.create(jurado=jurado, grado= grado, seccion=seccion, criterio_1=crit_01,
                             criterio_2=crit_02, criterio_3=crit_03, criterio_4=crit_04,
                             calificacion=calificacion)
        
        return redirect("/envio_exitoso/")


    return render(request ,"ingresar_baile.html")

def ingresar_playback(request):

    if request.method=="POST":
        grado = request.POST.get('grado')
        seccion = request.POST.get('seccion')
        jurado = request.POST.get('jurado')
        crit_01 = request.POST.get('crit01')
        crit_02 = request.POST.get('crit02')
        crit_03 = request.POST.get('crit03')
        crit_04 = request.POST.get('crit04')
        crit_05 = request.POST.get('crit05')
        crit_06 = request.POST.get('crit06')
        calificacion = int(crit_01)+int(crit_02)+int(crit_03)+int(crit_04)+int(crit_05)+int(crit_06)

        PlayBack.objects.create(jurado=jurado, grado= grado, seccion=seccion, criterio_1=crit_01,
                             criterio_2=crit_02, criterio_3=crit_03, criterio_4=crit_04, criterio_5=crit_05,
                             criterio_6=crit_06, calificacion=calificacion)
        
        return redirect("/envio_exitoso/")
    
    return render(request ,"ingresar_playback.html")


def inicio(request):

    return render(request, 'inicio.html')

def envio_exitoso(request):

    return render(request, 'envio_exitoso.html')

def buscar_puntaje(request):

    return render(request, "buscar_puntaje.html")

def mostrar_puntaje(request):

    if request.method=="POST":
        grado = request.POST.get('grado')
        seccion = request.POST.get('seccion')
        categoria = request.POST.get('categoria')
        if categoria=="CANTO":
            calificacion_1 = Canto.objects.filter(jurado__icontains="jurado 1", grado__icontains=grado, seccion__icontains=seccion)
            calificacion_2 = Canto.objects.filter(jurado__icontains="jurado 2", grado__icontains=grado, seccion__icontains=seccion)
            calificacion_3 = Canto.objects.filter(jurado__icontains="jurado 3", grado__icontains=grado, seccion__icontains=seccion)
            context = {"grado":grado, "seccion":seccion, "categoria":categoria,
                   "calif01":calificacion_1, "calif02":calificacion_2, "calif03":calificacion_3}
        elif categoria=="BAILE":
            calificacion_1 = Baile.objects.filter(jurado__icontains="jurado 1", grado__icontains=grado, seccion__icontains=seccion)
            calificacion_2 = Baile.objects.filter(jurado__icontains="jurado 2", grado__icontains=grado, seccion__icontains=seccion)
            calificacion_3 = Baile.objects.filter(jurado__icontains="jurado 3", grado__icontains=grado, seccion__icontains=seccion)
            context = {"grado":grado, "seccion":seccion, "categoria":categoria,
                   "calif01":calificacion_1, "calif02":calificacion_2, "calif03":calificacion_3}
        else:
            calificacion_1 = PlayBack.objects.filter(jurado__icontains="jurado 1", grado__icontains=grado, seccion__icontains=seccion)
            calificacion_2 = PlayBack.objects.filter(jurado__icontains="jurado 2", grado__icontains=grado, seccion__icontains=seccion)
            calificacion_3 = PlayBack.objects.filter(jurado__icontains="jurado 3", grado__icontains=grado, seccion__icontains=seccion)
            context = {"grado":grado, "seccion":seccion, "categoria":categoria,
                   "calif01":calificacion_1, "calif02":calificacion_2, "calif03":calificacion_3}
        
        return render(request, "mostrar_puntaje.html", context)


