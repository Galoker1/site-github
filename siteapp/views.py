from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

def main(request):
    return render(request,"siteapp/index.html")

#def book_detail(request,slug):
#    book = Book.objects.get(slug__iexact=slug)
#    return render(request,"siteapp/book_detail.html",context={'book':book})
class BookDetail(View):
    def get(self,request,slug):
        book = Book.objects.get(slug__iexact=slug)
        return render(request,"siteapp/book_detail.html",context={'book':book})
def book_list(request):
    books=Book.objects.all()
    return render(request,"siteapp/book_list.html",context={'books':books})

class BookCreate(LoginRequiredMixin,View):
    raise_exception=True
    def get(self,request):
        form=BookForm()
        return render(request,'siteapp/book_create.html',context={'form':form})
    def post(self,request):
            bound_form=BookForm(request.POST)
            print('-------')
            print(bound_form)
            print('-------')
            if bound_form.is_valid():
                new_post=bound_form.save()
                return redirect(new_post)
            return render(request,'siteapp/book_create.html',context={'form':bound_form})
class BookUpdate(LoginRequiredMixin,View):
    raise_exception=True
    def get(self,request,slug):
        book=Book.objects.get(slug__iexact=slug)
        bound_form= BookForm(instance=book)
        return render(request,'siteapp/book_update.html',context={'form':bound_form,"book":book})
    def post(self,request,slug):
            book=Book.objects.get(slug__iexact=slug)
            bound_form= BookForm(request.POST,instance=book)
            if bound_form.is_valid():
                new_post=bound_form.save()
                return redirect(new_post)
            return render(request,'siteapp/book_create.html',context={'form':bound_form})

class BookDelete(LoginRequiredMixin,View):
    raise_exception=True
    def get(self,request,slug):
        book=Book.objects.get(slug__iexact=slug)
        return render(request,'siteapp/book_delete.html',context={"book":book})
    def post(self,request,slug):
            book=Book.objects.get(slug__iexact=slug)
            book.delete()
            return redirect(reverse('book_list_url'))
