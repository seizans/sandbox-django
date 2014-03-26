# coding=utf8

from django.test import TestCase

from core.factories import StaffFactory


class FactoryBoyTest(TestCase):
    def setUp(self):
        pass

    def test_factory(self):
        staff1 = StaffFactory()
        print staff1.name
        print staff1.belong.name
        print staff1.company_name

        staff2 = StaffFactory()
        print staff2.name
        print staff2.belong.name
        print staff2.company_name
