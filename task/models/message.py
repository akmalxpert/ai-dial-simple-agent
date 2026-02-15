from dataclasses import dataclass
from typing import Any
import base64
from task.models.role import Role


@dataclass
class Message:
    role: Role
    content: str
    tool_call_id: str | None = None
    name: str| None = None
    tool_calls: list[dict[str, Any]] | None = None

    def to_dict(self) -> dict[str, Any]:
        result = {
            "role": self.role.value,
            "content": self.content
        }
        if self.tool_call_id:
            result["tool_call_id"] = self.tool_call_id
        if self.name:
            result["name"] = self.name
        if self.tool_calls:
            result["tool_calls"] = self.tool_calls
        for key, value in self.__dict__.items():
            if isinstance(value, bytes):
                result[key] = base64.b64encode(value).decode('utf-8')
        return result
