# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .input_chat_ml_message_role import InputChatMlMessageRole

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class InputChatMlMessage(pydantic.BaseModel):
    role: InputChatMlMessageRole = pydantic.Field(description="ChatML role (system|assistant|user|function_call)")
    content: str = pydantic.Field(description="ChatML content")
    name: typing.Optional[str] = pydantic.Field(description="ChatML name")
    continue_: typing.Optional[bool] = pydantic.Field(
        alias="continue", description="Whether to continue this message or return a new one"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}