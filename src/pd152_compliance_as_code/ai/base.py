from __future__ import annotations

from typing import Protocol


class AIProvider(Protocol):
    def complete(self, prompt: str) -> str: ...
    def chat(self, messages: list[dict]) -> str: ...


class NoopAIProvider:
    def complete(self, prompt: str) -> str:
        raise NotImplementedError("No AI provider configured")

    def chat(self, messages: list[dict]) -> str:
        raise NotImplementedError("No AI provider configured")
