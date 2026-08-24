from pydantic.alias_generators import to_camel
from pydantic import ConfigDict, BaseModel

class _CamelBase(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )