# blingua-sdk

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/advanced-setup/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_translate_wrapper_text_translate_target_lang_post(target_lang='<value>', request_body='<value>', api_key='<value>')

if res.text_result is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [BlinguaSDK](docs/sdks/blinguasdk/README.md)

* [text_translate_wrapper_text_translate_target_lang_post](docs/sdks/blinguasdk/README.md#text_translate_wrapper_text_translate_target_lang_post) - Text Translate Wrapper
* [detect_patterns_patterns_pattern_params_post](docs/sdks/blinguasdk/README.md#detect_patterns_patterns_pattern_params_post) - Detect Patterns
* [text_replace_wrapper_text_replace_replacement_rules_post](docs/sdks/blinguasdk/README.md#text_replace_wrapper_text_replace_replacement_rules_post) - Text Replace Wrapper
* [detect_ner_wrapper_text_detect_ner_ner_tags_post](docs/sdks/blinguasdk/README.md#detect_ner_wrapper_text_detect_ner_ner_tags_post) - Detect Ner Wrapper
* [text_summarize_wrapper_text_summarize_summary_length_post](docs/sdks/blinguasdk/README.md#text_summarize_wrapper_text_summarize_summary_length_post) - Text Summarize Wrapper
* [text_qna_wrapper_text_qna_question_post](docs/sdks/blinguasdk/README.md#text_qna_wrapper_text_qna_question_post) - Text Qna Wrapper
* [text_intent_wrapper_text_intent_post](docs/sdks/blinguasdk/README.md#text_intent_wrapper_text_intent_post) - Text Intent Wrapper
* [text_lemstem_wrapper_text_lemstem_operation_post](docs/sdks/blinguasdk/README.md#text_lemstem_wrapper_text_lemstem_operation_post) - Text Lemstem Wrapper
* [text_tokenize_wrapper_text_tokenize_post](docs/sdks/blinguasdk/README.md#text_tokenize_wrapper_text_tokenize_post) - Text Tokenize Wrapper
* [text_embed_wrapper_text_embed_task_type_post](docs/sdks/blinguasdk/README.md#text_embed_wrapper_text_embed_task_type_post) - Text Embed Wrapper
* [text_generate_wrapper_text_generate_length_post](docs/sdks/blinguasdk/README.md#text_generate_wrapper_text_generate_length_post) - Text Generate Wrapper
* [detect_spam_wrapper_text_detect_spam_post](docs/sdks/blinguasdk/README.md#detect_spam_wrapper_text_detect_spam_post) - Detect Spam Wrapper
* [text_clean_wrapper_text_clean_post](docs/sdks/blinguasdk/README.md#text_clean_wrapper_text_clean_post) - Text Clean Wrapper
* [text_normalize_wrapper_text_normalize_post](docs/sdks/blinguasdk/README.md#text_normalize_wrapper_text_normalize_post) - Text Normalize Wrapper
* [text_spellcheck_wrapper_text_spellcheck_post](docs/sdks/blinguasdk/README.md#text_spellcheck_wrapper_text_spellcheck_post) - Text Spellcheck Wrapper
* [text_srl_wrapper_text_srl_post](docs/sdks/blinguasdk/README.md#text_srl_wrapper_text_srl_post) - Text Srl Wrapper
* [text_cluster_wrapper_text_cluster_post](docs/sdks/blinguasdk/README.md#text_cluster_wrapper_text_cluster_post) - Text Cluster Wrapper
* [text_sentiment_wrapper_text_sentiment_post](docs/sdks/blinguasdk/README.md#text_sentiment_wrapper_text_sentiment_post) - Text Sentiment Wrapper
* [text_topic_wrapper_text_topic_post](docs/sdks/blinguasdk/README.md#text_topic_wrapper_text_topic_post) - Text Topic Wrapper
* [text_parts_of_speech_wrapper_text_parts_of_speech_post](docs/sdks/blinguasdk/README.md#text_parts_of_speech_wrapper_text_parts_of_speech_post) - Text Parts Of Speech Wrapper
* [text_paraphrase_wrapper_text_paraphrase_post](docs/sdks/blinguasdk/README.md#text_paraphrase_wrapper_text_paraphrase_post) - Text Paraphrase Wrapper
* [text_segment_wrapper_text_segment_post](docs/sdks/blinguasdk/README.md#text_segment_wrapper_text_segment_post) - Text Segment Wrapper
* [text_badness_wrapper_text_toxic_analysis_type_post](docs/sdks/blinguasdk/README.md#text_badness_wrapper_text_toxic_analysis_type_post) - Text Badness Wrapper
* [text_emojis_wrapper_text_replace_emojis_post](docs/sdks/blinguasdk/README.md#text_emojis_wrapper_text_replace_emojis_post) - Text Emojis Wrapper
* [text_tfidf_wrapper_text_tfidf_post](docs/sdks/blinguasdk/README.md#text_tfidf_wrapper_text_tfidf_post) - Text Tfidf Wrapper
* [text_idioms_wrapper_text_idioms_post](docs/sdks/blinguasdk/README.md#text_idioms_wrapper_text_idioms_post) - Text Idioms Wrapper
* [text_sense_disambiguation_wrapper_text_sense_disambiguation_post](docs/sdks/blinguasdk/README.md#text_sense_disambiguation_wrapper_text_sense_disambiguation_post) - Text Sense Disambiguation Wrapper
* [text_frequency_wrapper_text_frequency_post](docs/sdks/blinguasdk/README.md#text_frequency_wrapper_text_frequency_post) - Text Frequency Wrapper
* [text_anomaly_wrapper_text_anomaly_post](docs/sdks/blinguasdk/README.md#text_anomaly_wrapper_text_anomaly_post) - Text Anomaly Wrapper
* [text_core_reference_wrapper_text_core_reference_post](docs/sdks/blinguasdk/README.md#text_core_reference_wrapper_text_core_reference_post) - Text Core Reference Wrapper
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

### Example

```python
import blinguasdk
from blinguasdk.models import errors

s = blinguasdk.BlinguaSDK()


res = None
try:
    res = s.text_translate_wrapper_text_translate_target_lang_post(target_lang='<value>', request_body='<value>', api_key='<value>')
except errors.HTTPValidationError as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.text_result is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://rcd.nscampfire.com` | None |

#### Example

```python
import blinguasdk

s = blinguasdk.BlinguaSDK(
    server_idx=0,
)


res = s.text_translate_wrapper_text_translate_target_lang_post(target_lang='<value>', request_body='<value>', api_key='<value>')

if res.text_result is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import blinguasdk

s = blinguasdk.BlinguaSDK(
    server_url="https://rcd.nscampfire.com",
)


res = s.text_translate_wrapper_text_translate_target_lang_post(target_lang='<value>', request_body='<value>', api_key='<value>')

if res.text_result is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import blinguasdk
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = blinguasdk.BlinguaSDK(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
