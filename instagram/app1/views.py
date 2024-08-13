from django.shortcuts import render,redirect
from app1.models import Author,Book
from django.contrib import messages

# Create your views here.
def home(request):
    obj=Book.objects.all()
    if request.method=="POST":
        ser=request.POST.get("search")
        obj=Book.objects.filter(title__icontains=ser)
    return render(request,"home.html",{"books":obj})

def bookView(request):
    if request.method=="POST":
        book1=request.POST.get("bname")
        price1=request.POST.get("price")
        genre1=request.POST.get("genre")
        no=request.POST.get("sno")
        if Author.objects.filter(id=no).exists():
            a=Author.objects.get(id=no)
            obj=Book(title=book1,price=price1,genre=genre1,author=a)
            obj.save()
            messages.success(request,"Congratulations mama you Regestered a book")
            return render(request,"book.html",{"books":obj})
        else:
            return redirect("bookpage")
    return render(request,"book.html")
def authorView(request):
    if request.method=="POST":
        a=request.POST.get("aname")
        b=request.POST.get("age")
        c=request.POST.get("rate")
        p=request.FILES.get("pic")
        obj=Author(name=a,age=b,rate=c,image=p)
        obj.save()
        return render(request,"author.html",{"books":obj})
    return render(request,"author.html")

