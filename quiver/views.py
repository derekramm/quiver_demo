from django.shortcuts import *

# Create your views here.
from quiver.utils.quiver_helper import *

root = get_root()


def book_list(request):
    title = 'quiver book_list'
    book = root
    return render(request, 'quiver/book_list.html', locals())


def book_detail(request, uuid):
    title = 'quiver book_detail'
    book = get_book_by_uuid(uuid)
    return render(request, 'quiver/book_detail.html', locals())


def note_detail(request, uuid):
    title = 'quiver note_detail'
    note = get_note_by_uuid(uuid)
    return render(request, 'quiver/note_detail.html', locals())
