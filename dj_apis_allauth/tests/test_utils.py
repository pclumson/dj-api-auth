from django.test import TestCase

from dj_apis_allauth.utils import format_lazy


class TestFormatLazy(TestCase):
    def test_it_should_work(self):
        obj = format_lazy("{} {}", "arst", "zxcv")

        self.assertNotIsInstance(obj, str)
        self.assertEqual(str(obj), "arst zxcv")
