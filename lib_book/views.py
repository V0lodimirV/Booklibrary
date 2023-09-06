from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Book, Reader, BorrowedBook
from .forms import ReaderForm


def home(request):
    form = ReaderForm()

    if request.method == "POST":
        last_name = request.POST["last_name"]
        first_name = request.POST["first_name"]
        patronymic = request.POST["patronymic"]

        existing_reader = Reader.objects.filter(
            last_name=last_name, first_name=first_name, patronymic=patronymic
        ).first()

        if existing_reader:
            messages.error(
                request, "Пользователь с такими данными уже зарегистрирован."
            )
            return render(
                request, "home.html", {"readers": Reader.objects.all(), "form": form}
            )
        else:
            reader = Reader.objects.create(
                last_name=last_name, first_name=first_name, patronymic=patronymic
            )
            return redirect("reader_detail", reader_id=reader.id)

    readers = Reader.objects.all()
    return render(request, "home.html", {"readers": readers, "form": form})


def reader_detail(request, reader_id):
    reader = Reader.objects.get(id=reader_id)
    books = Book.objects.filter(available=True)
    borrowed_books = BorrowedBook.objects.filter(
        reader=reader, returned_date__isnull=True
    )
    return render(
        request,
        "reader_detail.html",
        {"reader": reader, "books": books, "borrowed_books": borrowed_books},
    )


def borrow_book(request, reader_id):
    if request.method == "POST":
        reader = Reader.objects.get(id=reader_id)
        book_id = request.POST["book"]
        book = Book.objects.get(id=book_id)
        if book.available:
            borrowed_book = BorrowedBook(
                reader=reader, book=book, borrowed_date=timezone.now()
            )
            borrowed_book.save()
            book.available = False
            book.save()
        return redirect("reader_detail", reader_id=reader_id)


def return_book(request, reader_id):
    if request.method == "POST":
        reader = Reader.objects.get(id=reader_id)
        borrowed_book_id = request.POST["borrowed_book"]
        borrowed_book = BorrowedBook.objects.get(
            id=borrowed_book_id, reader=reader, returned_date__isnull=True
        )
        borrowed_book.returned_date = timezone.now()
        borrowed_book.save()
        book = borrowed_book.book
        book.available = True
        book.save()
    return redirect("book_detail", reader_id=reader_id)


def book_detail(request, reader_id):
    reader = Reader.objects.get(id=reader_id)
    books = Book.objects.filter(available=True)
    borrowed_books = BorrowedBook.objects.filter(
        reader=reader, returned_date__isnull=True
    )
    return render(
        request,
        "book_detail.html",
        {"reader": reader, "books": books, "borrowed_books": borrowed_books},
    )


def return_detail(request, reader_id):
    reader = Reader.objects.get(id=reader_id)
    books = Book.objects.filter(available=True)
    borrowed_books = BorrowedBook.objects.filter(
        reader=reader, returned_date__isnull=True
    )
    return render(
        request,
        "return_detail.html",
        {"reader": reader, "books": books, "borrowed_books": borrowed_books},
    )
