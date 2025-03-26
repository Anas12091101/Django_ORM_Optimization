from django.core.management.base import BaseCommand
from blog.models import Author, Book
from faker import Faker
from tqdm import tqdm

fake = Faker()

class Command(BaseCommand):
    help = "Populate the database with sample data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating authors and books...")

        for _ in tqdm(range(5000)):  # Create 1000 authors
            author = Author.objects.create(name=fake.name())

            # Create 100 books for each author
            books = [
                Book(title=fake.sentence(), author=author, published_date=fake.date())
                for _ in range(100)
            ]
            Book.objects.bulk_create(books)

        self.stdout.write(self.style.SUCCESS("Successfully populated the database!"))
