from django.test import TestCase

from ddd.post.post import Post
from test.post.valueobjects.test_id import IdTests
from test.post.valueobjects.test_title import TitleTests


class PostTests(TestCase):
    @classmethod
    def obj(cls) -> Post:
        return Post(IdTests.obj(), TitleTests.obj())

    def test_init(self):
        """インスタンス作成できること"""
        obj = PostTests.obj()
        self.assertIsNotNone(obj)

    def test_init_invalid(self):
        """引数nullでインスタンス作成できないこと"""
        with self.assertRaises(ValueError):
            # noinspection PyTypeChecker
            Post(None, TitleTests.obj())

        """引数nullでインスタンス作成できないこと"""
        with self.assertRaises(ValueError):
            # noinspection PyTypeChecker
            Post(IdTests.obj(), None)

    def test_equals(self):
        """idで同じインスタンスと判断されること"""
        obj1 = PostTests.obj()
        obj2 = PostTests.obj()
        self.assertEqual(obj1, obj2)

        """idで異なるインスタンスと判断されること"""
        obj3 = Post(IdTests.obj2(), TitleTests.obj())
        self.assertNotEqual(obj1, obj3)

    def test_immutable(self):
        """イミュータブルであること"""
        obj = PostTests.obj()
        with self.assertRaises(ValueError):
            obj.id = IdTests.obj2()

    def test_mutable(self):
        """ミュータブルであること"""
        obj = PostTests.obj()
        obj.title = TitleTests.obj2()
        self.assertIsNotNone(obj)
        self.assertEqual(obj.title, TitleTests.obj2())
