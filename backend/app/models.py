from beanie import Document

class User(Document):
    taskname: str
    taskdesk: str
    desc: bool
