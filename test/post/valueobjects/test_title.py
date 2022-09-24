from dataclasses import FrozenInstanceError
from django.test import TestCase
from ddd.post.valueobjects.title import Title


class TitleTests(TestCase):
    @classmethod
    def obj(cls) -> Title:
        return Title('title')

    @classmethod
    def obj2(cls) -> Title:
        return Title('title2')

    def test_init(self):
        """インスタンス作成できること"""
        obj = TitleTests.obj()
        self.assertIsNotNone(obj)

    def test_init_too_short(self):
        """0文字でインスタンス作成できないこと"""
        with self.assertRaises(ValueError):
            Title("")

    def test_init_too_long(self):
        """7文字でインスタンス作成できないこと"""
        with self.assertRaises(ValueError):
            Title("1234567")

    def test_init_null(self):
        """nullでインスタンス作成できないこと"""
        with self.assertRaises(TypeError):
            # noinspection PyArgumentList
            Title()

    def test_equals(self):
        """値で同じインスタンスと判断されること"""
        obj1 = Title('title')
        obj2 = Title('title')
        self.assertEqual(obj1, obj2)

        """値で異なるインスタンスと判断されること"""
        obj3 = Title('other')
        self.assertNotEqual(obj1, obj3)

    def test_immutable(self):
        """イミュータブルであること"""
        obj = TitleTests.obj()
        with self.assertRaises(FrozenInstanceError):
            # noinspection PyDataclass
            obj.title = "other"
