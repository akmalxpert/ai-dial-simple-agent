from typing import Any

from task.tools.users.base import BaseUserServiceTool
from task.tools.users.models.user_info import UserUpdate


class UpdateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return 'update_user'

    @property
    def description(self) -> str:
        return 'Update the user info'

    @property
    def input_schema(self) -> dict[str, Any]:
        params = {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "User ID that should be updated"
                }
            },
            "required": [
                "id"
            ]
        }
        params['properties']['new_info'] = UserUpdate.model_json_schema()
        return params

    def execute(self, arguments: dict[str, Any]) -> str:
        user_id = arguments['id']
        update_user = UserUpdate.model_validate(arguments['new_info'])
        try:
            self._user_client.update_user(user_id, update_user)
        except Exception as e:
            return f"Error while creating a new user: {str(e)}"
