import json
import os

from quiver.models import *

QUIVER_PATH = os.path.abspath('static/Quiver.qvlibrary')
ROOT_JSON_PATH = os.path.join(QUIVER_PATH, 'meta.json')
BOOKS = dict()
NOTES = dict()


def get_json_data(json_path=ROOT_JSON_PATH):
    with open(json_path, 'r') as f:
        return json.load(f)


def get_root_book(path=QUIVER_PATH):
    json_data = get_json_data()
    uuid = json_data.get('uuid')
    name = json_data.get('uuid')
    children = json_data.get('children')
    path = path
    root_book = QvNoteBook(uuid=uuid, name=name, children=children, path=path)
    BOOKS[root_book.uuid] = root_book
    return root_book


def get_child_books(parent_book):
    for child in parent_book.children:
        uuid = child.get('uuid')
        path = os.path.join(QUIVER_PATH, f'{uuid}.qvnotebook')  # 文件夹存储的时候使用扁平结构，都在根目录下
        name = get_json_data(os.path.join(path, 'meta.json')).get('name')
        children = child.get('children')
        book = QvNoteBook(uuid=uuid, name=name, children=children, path=path)

        book.parent = parent_book
        get_notes(book)  # 获取笔记
        BOOKS[book.uuid] = book  # 存到字典中便于查找

        get_child_books(book)  # 递归
        parent_book.notebooks.append(book)
    return parent_book.notebooks


def get_root(path=QUIVER_PATH):
    # 获取根节点
    root_book = get_root_book(path)
    # 添加收件箱
    root_book.notebooks.append(QvNoteBook('Inbox', 'Inbox', None, os.path.join(QUIVER_PATH, 'Inbox.qvnotebook')))
    # 添加垃圾箱
    root_book.notebooks.append(QvNoteBook('Trash', 'Trash', None, os.path.join(QUIVER_PATH, 'Trash.qvnotebook')))
    # 递归添加子节点
    get_child_books(root_book)
    return root_book


def get_notes(book):
    book.notes.clear()
    qvnotes = [note for note in os.listdir(book.path) if note.endswith('.qvnote')]
    for n in qvnotes:
        path = os.path.join(book.path, n)
        json_data = get_json_data(os.path.join(path, 'meta.json'))
        uuid = json_data.get('uuid')
        title = json_data.get('title')
        created_at = json_data.get('created_at')
        updated_at = json_data.get('updated_at')
        tags = json_data.get('tags')
        note = QvNote(uuid, title, created_at, updated_at, tags, path)
        note.cells = get_cells(note)
        book.notes.append(note)
        note.book = book
        NOTES[note.uuid] = note
    return book.notes


def get_cells(note):
    json_data = get_json_data(os.path.join(note.path, 'content.json'))
    for c in json_data.get('cells'):
        cell = QvCell(c.get('type'), c.get('language'), c.get('data'))
        path = note.path[note.path.find('/static/'):]
        cell.data = cell.data.replace('quiver-image-url', path + '/resources')
        note.cells.append(cell)
        cell.note = note
    return note.cells


def get_book_by_uuid(uuid):
    book = BOOKS.get(uuid)
    return book


def get_note_by_uuid(uuid):
    note = NOTES.get(uuid)
    return note
