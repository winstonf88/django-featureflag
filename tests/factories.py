import factory

from .models import Person


class PersonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Person

    name = factory.Faker("name")


class FeatureFlagFactory(factory.DjangoModelFactory):
    class Meta:
        model = "featureflag.FeatureFlag"

    name = factory.Faker("word")


class FlaggedObjectFactory(factory.DjangoModelFactory):
    class Meta:
        model = "featureflag.FlaggedObject"

    feature_flag = factory.SubFactory(FeatureFlagFactory)
