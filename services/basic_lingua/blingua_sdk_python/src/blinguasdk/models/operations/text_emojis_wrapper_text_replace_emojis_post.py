"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import textresult as components_textresult
from typing import Optional


@dataclasses.dataclass
class TextEmojisWrapperTextReplaceEmojisPostRequest:
    UNSET='__SPEAKEASY_UNSET__'
    request_body: str = dataclasses.field(metadata={'request': { 'media_type': 'text/plain' }})
    api_key: Optional[str] = dataclasses.field(default=UNSET, metadata={'header': { 'field_name': 'api-key', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class TextEmojisWrapperTextReplaceEmojisPostResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    text_result: Optional[components_textresult.TextResult] = dataclasses.field(default=None)
    r"""Successful Response"""
    

