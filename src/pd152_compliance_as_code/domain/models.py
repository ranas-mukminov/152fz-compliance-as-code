from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class OperatorContacts:
    address: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None


@dataclass
class Operator:
    name: str
    inn: Optional[str] = None
    ogrn: Optional[str] = None
    contacts: OperatorContacts = field(default_factory=OperatorContacts)


@dataclass
class Processor:
    name: str
    role: Optional[str] = None
    contacts: OperatorContacts = field(default_factory=OperatorContacts)


@dataclass
class DataSubjectCategory:
    id: str
    name: str
    description: Optional[str] = None


@dataclass
class PersonalDataCategory:
    id: str
    name: str
    fields: List[str]
    sensitivity: str = "standard"  # standard | special | biometric


@dataclass
class RetentionPolicy:
    description: str
    period: Optional[str] = None


@dataclass
class SecurityMeasures:
    org: List[str] = field(default_factory=list)
    tech: List[str] = field(default_factory=list)
    legal: List[str] = field(default_factory=list)


@dataclass
class ProcessingActivity:
    id: str
    name: str
    subjects: List[str]
    data_categories: List[str]
    purposes: List[str]
    legal_basis: List[str]
    operations: List[str]
    storage_locations: List[str] = field(default_factory=list)
    recipients: List[str] = field(default_factory=list)
    retention: RetentionPolicy = field(default_factory=lambda: RetentionPolicy(description=""))
    security_measures: SecurityMeasures = field(default_factory=SecurityMeasures)
    notes: Optional[str] = None


@dataclass
class ComplianceConfig:
    operator: Operator
    processors: List[Processor] = field(default_factory=list)
    data_subjects: List[DataSubjectCategory] = field(default_factory=list)
    personal_data_categories: List[PersonalDataCategory] = field(default_factory=list)
    processing_activities: List[ProcessingActivity] = field(default_factory=list)

    def find_subject(self, subject_id: str) -> Optional[DataSubjectCategory]:
        return next((s for s in self.data_subjects if s.id == subject_id), None)

    def find_data_category(self, category_id: str) -> Optional[PersonalDataCategory]:
        return next((c for c in self.personal_data_categories if c.id == category_id), None)
