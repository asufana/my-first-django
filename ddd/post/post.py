from ddd.post.valueobjects.id import Id
from ddd.post.valueobjects.title import Title


class Post:
    def __init__(self, id: Id, title: Title):
        if id is None:
            raise ValueError("invalid error")
        if title is None:
            raise ValueError("invalid error")
        self.__id: Id = id
        self.__title: Title = title

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Post):
            return self.__id == other.__id
        return False

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        raise ValueError("invalid error")

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

