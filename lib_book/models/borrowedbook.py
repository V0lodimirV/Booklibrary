from django.db import models

from lib_book.models.book import Book
from lib_book.models.reader import Reader


class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField()
    returned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.reader} взял {self.book} - {self.borrowed_date}"
