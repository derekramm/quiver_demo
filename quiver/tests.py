from django.test import TestCase

# Create your tests here.
from quiver.utils.quiver_helper import *

root = get_root()

book_personal = root.notebooks[3]
book_derek = book_personal.notebooks[0]

book_tour = root.notebooks[2]

note_10 = book_tour.notes[9]

print()

