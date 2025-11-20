from pd152_compliance_as_code.yaml_schema.validator import validate_mapping


def test_invalid_reference_detected():
    data = {
        "operator": {"name": "Test"},
        "data_subjects": [{"id": "s1", "name": "S1"}],
        "personal_data_categories": [{"id": "c1", "name": "C1", "fields": ["f1"]}],
        "processing_activities": [
            {
                "id": "p1",
                "name": "Proc",
                "subjects": ["unknown"],
                "data_categories": ["c1"],
                "purposes": ["test"],
                "legal_basis": ["договор"],
                "operations": ["сбор"],
                "retention": {"description": "1"},
            }
        ],
    }
    errors = validate_mapping(data)
    assert any("unknown" in e for e in errors)
