from typing import Any

from task.tools.users.base import BaseUserServiceTool
from task.tools.users.models.user_info import UserCreate


class CreateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return 'add_user'

    @property
    def description(self) -> str:
        return 'Tool to add user'

    @property
    def input_schema(self) -> dict[str, Any]:
        return UserCreate.model_json_schema()

    def execute(self, arguments: dict[str, Any]) -> str:
        try:
            return self._user_client.add_user(UserCreate.model_validate(arguments))
        except Exception as e:
            return f"Error while creating a new user: {str(e)}"
