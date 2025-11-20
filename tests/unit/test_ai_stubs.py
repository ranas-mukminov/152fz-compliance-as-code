import pytest

from pd152_compliance_as_code.ai.base import NoopAIProvider
from pd152_compliance_as_code.ai.policy_parser import draft_yaml_from_policy


def test_noop_provider_raises():
    provider = NoopAIProvider()
    with pytest.raises(NotImplementedError):
        provider.complete("test")


def test_draft_yaml_basic():
    text = "В политике указано, что данные пациентов хранятся и используются для оказания медицинских услуг."
    yaml_text = draft_yaml_from_policy(text)
    assert "patients" in yaml_text
