from pd152_compliance_as_code.domain.models import ComplianceConfig, Operator, ProcessingActivity, RetentionPolicy, SecurityMeasures


def test_activity_requires_purposes():
    cfg = ComplianceConfig(
        operator=Operator(name="X"),
        data_subjects=[],
        personal_data_categories=[],
        processing_activities=[
            ProcessingActivity(
                id="p1",
                name="Proc",
                subjects=[],
                data_categories=[],
                purposes=["purpose"],
                legal_basis=["договор"],
                operations=["сбор"],
                retention=RetentionPolicy(description="1"),
                security_measures=SecurityMeasures(),
            )
        ],
    )
    assert cfg.processing_activities[0].purposes
