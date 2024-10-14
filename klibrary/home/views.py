from django.shortcuts import render,redirect,get_object_or_404
from .forms import Book_list
from .models import Books
# Create your views here.
def home(request):
    return render(request, 'index/home.html')

def about(request):
    return render(request, 'index/about.html')

def services(request):
    return render(request, 'index/services.html')

def books(request,):
    dict_book={
        'Book': Books.objects.all()
    }
    return render(request, 'index/books.html',dict_book)

def add(request):
     if request.method == 'POST':
        form = Book_list(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()  # Save the form if it's valid
            return redirect('books')  # Redirect to your book list page after saving
     else:
        form = Book_list()
    
     return render(request, 'crud/add.html', {'form':form})

def edit(request, pk):
    instance_edit = get_object_or_404(Books, pk=pk)  # Safely get the instance

    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        email = request.POST.get('email')
        
        # Handle image upload
        image = request.FILES.get('image')  # Use request.FILES for uploaded files

        # Update the instance fields
        instance_edit.name = name
        instance_edit.desc = desc
        instance_edit.price = price
        instance_edit.email = email
        
        if image:  # Check if an image was uploaded
            instance_edit.image = image
        
        instance_edit.save()  # Save changes to the instance
        return redirect('books')  # Redirect to a success page after saving

    form = Book_list(instance=instance_edit)  # Load the form with the existing instance data
    return render(request, 'crud/edit.html', {'form': form})

def delete(request,pk):
    instance = Books.objects.get(pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('books')  # Redirect to your book list page after deletion
    
    return render(request, 'crud/delete.html', {'book': instance})