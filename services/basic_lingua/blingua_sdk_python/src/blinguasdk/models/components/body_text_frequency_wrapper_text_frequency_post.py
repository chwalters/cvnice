"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from blinguasdk import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyTextFrequencyWrapperTextFrequencyPost:
    UNSET='__SPEAKEASY_UNSET__'
    user_input: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_input') }})
    words: Optional[List[str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('words'), 'exclude': lambda f: f is BodyTextFrequencyWrapperTextFrequencyPost.UNSET }})
    

