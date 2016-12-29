from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.
    num_genre=Genre.objects.count()
    num_specificbook=Book.objects.filter(title='BOOK1').count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'catalog/index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,'num_genre':num_genre,'num_specificbook': num_specificbook,'num_visits':num_visits},
    )
from django.views import generic
def books(request):
    queryset = Book.objects.all()
    return render(request, 'catalog/book_list.html', context={'queryset': queryset})
from django.http import  Http404
class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 10
    def book_detail_view(request, pk):
        try:
            book_id = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")

        # book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'book_detail.html',
            context={'book': book_id, }
        )
def authors(request):
    query=Author.objects.all()
    return render(request,'catalog/author_list.html',context={'query':query})

def AuthorDetailView(request,pk):
    author_id=Author.objects.get(id=pk)
    return render(request,'catalog/author_detail.html',context={'author_id':author_id})
