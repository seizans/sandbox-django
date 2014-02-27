# coding=utf8
import string

import factory
from factory.fuzzy import FuzzyText

from core.models import Company, Staff


class CompanyFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Company
    id = factory.Sequence(lambda n: n)
    name = FuzzyText(prefix='1499', length=9, chars=string.digits)
    # name = factory.LazyAttribute(lambda o: '会社名{}'.format(o.id))


class StaffFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Staff
    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda o: 'スタッフ名{}'.format(o.id))
    belong = factory.SubFactory(CompanyFactory)

    company_name = factory.LazyAttribute(lambda o: o.belong.name)
