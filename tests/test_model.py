import pytest

from featureflag.models import FeatureFlag, FlaggedObject

from .factories import FeatureFlagFactory, FlaggedObjectFactory, PersonFactory

pytestmark = pytest.mark.django_db


class TestFlaggedObject:
    def test_content_object(self):
        person = PersonFactory.create()
        flagged_object = FlaggedObjectFactory.create(content_object=person)

        assert flagged_object.content_object == person
        assert flagged_object.object_id == person.id


class TestFeatureFlag:
    def test_get_returns_created_flag(self):
        name = "FOO"
        flag = FeatureFlagFactory.create(name=name)

        assert FeatureFlag.get(name) == flag

    def test_get_creates_if_auto_create_enabled(self, settings):
        settings.FEATURE_FLAG = {"CREATE_MISSING": True}
        assert FeatureFlag.get("OPS")

    def test_get_creates_with_settings_default(self, settings):
        settings.FEATURE_FLAG = {"CREATE_MISSING": True, "CREATE_DEFAULT": True}

        flag = FeatureFlag.get("OPS")
        assert flag.everyone is True

    def test_get_raises_if_auto_create_disabled(self, settings):
        settings.FEATURE_FLAG = {"CREATE_MISSING": False}
        with pytest.raises(FeatureFlag.DoesNotExist):
            FeatureFlag.get("OPS")

    def test_is_active_true_for_everyone(self):
        flag = FeatureFlagFactory.create(everyone=True)
        person = PersonFactory.create()

        assert flag.is_active() is True
        assert flag.is_active(person) is True

    def test_is_active_false_for_everyone(self):
        person = PersonFactory.create()
        flag = FeatureFlag.objects.create(everyone=False)
        FlaggedObjectFactory.create(content_object=person, feature_flag=flag)

        assert flag.is_active() is False
        assert flag.is_active(person) is False

    def test_is_active_for_obj(self, faker):
        inactive = PersonFactory.create()
        active = PersonFactory.create()
        flag = FeatureFlag.objects.create(everyone=None)
        FlaggedObject.objects.create(content_object=active, feature_flag=flag)

        assert flag.is_active() is False
        assert flag.is_active(inactive) is False
        assert flag.is_active(active) is True
