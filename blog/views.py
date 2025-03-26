from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import Length
from blog.models import Author, Book
import time

# 1. BAD QUERY: N+1 Problem
# Example Use Case: Fetching books and their authors
def bad_query_foreign_key(request):
    start_time = time.time()
    books = Book.objects.all()  # Fetches all books but does not fetch authors

    data = []
    for book in books:
        data.append({"title": book.title, "author": book.author.name})  # Extra query for each book

    end_time = time.time()
    return JsonResponse({"books": data, "query_time": end_time - start_time})

# GOOD QUERY: Using select_related to fix N+1
def good_query_foreign_key(request):
    start_time = time.time()
    books = Book.objects.select_related("author").all()  # Fetches books + authors in one query

    data = [{"title": book.title, "author": book.author.name} for book in books]

    end_time = time.time()
    return JsonResponse({"books": data, "query_time": end_time - start_time})

# 2. BAD QUERY: Multiple Queries for Aggregation
# Example Use Case: Counting books per author
def bad_query_aggregation(request):
    start_time = time.time()
    authors = Author.objects.all()

    data = []
    for author in authors:
        book_count = author.books.count()  # Triggers a separate COUNT query for each author
        data.append({"author": author.name, "book_count": book_count})

    end_time = time.time()
    return JsonResponse({"authors": data, "query_time": end_time - start_time})

# GOOD QUERY: Using annotate to optimize aggregation
def good_query_aggregation(request):
    start_time = time.time()
    authors = Author.objects.annotate(book_count=Count("books")).all()  # Single query with COUNT

    data = [{"author": author.name, "book_count": author.book_count} for author in authors]

    end_time = time.time()
    return JsonResponse({"authors": data, "query_time": end_time - start_time})

# 3. BAD QUERY: Inefficient Filtering with Loops
# Example Use Case: Fetching books published after 2015
def bad_query_filtering(request):
    start_time = time.time()
    books = Book.objects.all()  # Fetch all books

    filtered_books = []
    for book in books:
        if book.published_date.year > 2015:  # Filtering in Python (slow)
            filtered_books.append({"title": book.title, "published_date": book.published_date})

    end_time = time.time()
    return JsonResponse({"books": filtered_books, "query_time": end_time - start_time})

# GOOD QUERY: Filtering at the database level
def good_query_filtering(request):
    start_time = time.time()
    books = Book.objects.filter(published_date__year__gt=2015).all()  # Filtering in SQL

    data = [{"title": book.title, "published_date": book.published_date} for book in books]

    end_time = time.time()
    return JsonResponse({"books": data, "query_time": end_time - start_time})

# 4. BAD QUERY: Inefficient Many-to-Many Prefetching
# Example Use Case: Loading all books of multiple authors
def bad_query_many_to_many(request):
    start_time = time.time()
    authors = Author.objects.all()  # Fetches authors, but lazy loads books

    data = []
    for author in authors:
        books = author.books.all()  # Triggers an extra query per author
        data.append({"author": author.name, "books": [book.title for book in books]})

    end_time = time.time()
    return JsonResponse({"authors": data, "query_time": end_time - start_time})

# GOOD QUERY: Using prefetch_related to fetch books efficiently
def good_query_many_to_many(request):
    start_time = time.time()
    authors = Author.objects.prefetch_related("books").all()  # Fetches authors + books in two queries

    data = [{"author": author.name, "books": [book.title for book in author.books.all()]} for author in authors]

    end_time = time.time()
    return JsonResponse({"authors": data, "query_time": end_time - start_time})
