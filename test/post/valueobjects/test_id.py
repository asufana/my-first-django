from dataclasses import FrozenInstanceError
from django.test import TestCase
from ddd.post.valueobjects.id import Id


class IdTests(TestCase):
    @classmethod
    def obj(cls) -> Id:
        return Id(1)

    @classmethod
    def obj2(cls) -> Id:
        return Id(2)

    def test_init(self):
        """インスタンス作成できること"""
        obj = IdTests.obj()
        self.assertIsNotNone(obj)

    def test_init_invalid(self):
        """0でインスタンス作成できないこと"""
        with self.assertRaises(ValueError):
            Id(0)

        """マイナス値でインスタンス作成できないこと"""
        with self.assertRaises(ValueError):
            Id(-1)

    def test_init_null(self):
        """nullでインスタンス作成できないこと"""
        with self.assertRaises(TypeError):
            # noinspection PyArgumentList
            Id()

    def test_equals(self):
        """値で同じインスタンスと判断されること"""
        obj1 = Id(1)
        obj2 = Id(1)
        self.assertEqual(obj1, obj2)

        """値で異なるインスタンスと判断されること"""
        obj3 = Id(2)
        self.assertNotEqual(obj1, obj3)

    def test_immutable(self):
        """イミュータブルであること"""
        obj = IdTests.obj()
        with self.assertRaises(FrozenInstanceError):
            # noinspection PyDataclass
            obj.id = "2"
