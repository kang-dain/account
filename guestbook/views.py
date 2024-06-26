from django.shortcuts import render, redirect
from django import forms
from .models import GuestBook

class WriteForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ['name', 'password', 'contents']
        widgets = {
            'password': forms.PasswordInput(),  # 비밀번호 입력을 위한 PasswordInput 위젯
        }

def write(request):
    if request.method == 'POST':
        form = WriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/guestbook/')
        else:
            return render(request, 'writeguestbook.html', {'form': form})
    else:
        form = WriteForm()
        return render(request, 'writeguestbook.html', {'form': form})

def guestbook(request):
    books = GuestBook.objects.all().order_by('-write_time')
    return render(request, 'guestbook.html', {'books': books})

def deleteform(request, id=0):
    return render(request, 'deleteform.html', {'id': id})

def delete(request):
    if request.method == "POST":
        id = request.POST['idval']
        password = request.POST['password']

        try:
            guestbook_entry = GuestBook.objects.get(id=id)
            if guestbook_entry.password == password:
                guestbook_entry.delete()
                return redirect('/guestbook/')
            else:
                return render(request, 'deleteform.html', {'id': id, 'error': 'Incorrect password'})
        except GuestBook.DoesNotExist:
            return redirect('/guestbook/')
    else:
        return redirect('/guestbook/')
