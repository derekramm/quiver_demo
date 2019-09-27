# Create your models here.
class QvNoteBook:
    def __init__(self, uuid, name, children, path):
        self.uuid = uuid
        self.name = name
        self.children = children if children else []
        self.path = path
        self.notebooks = []
        self.notes = []
        self.parent = None


class QvNote:
    def __init__(self, uuid, title, created_at, updated_at, tags, path):
        self.uuid = uuid
        self.title = title
        self.created_at = created_at
        self.updated_at = updated_at
        self.tags = tags
        self.path = path
        self.cells = []
        self.book = None


class QvCell:
    def __init__(self, qv_type, language, data):
        self.qv_type = qv_type
        self.language = language
        self.data = data
        self.note = None
