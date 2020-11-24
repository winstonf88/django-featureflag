import pytest

from featureflag.models import FeatureFlag
from featureflag.utils import is_active

from .factories import FeatureFlagFactory, PersonFactory

pytestmark = pytest.mark.django_db


class TestIsActive:
    def test_calls_model_is_active_method(self, mocker):
        person = PersonFactory.create()
        flag = FeatureFlagFactory.create()
        mock_is_active = mocker.patch.object(FeatureFlag, "is_active")

        is_active(flag.name, person)
        mock_is_active.assert_called_once_with(person)
