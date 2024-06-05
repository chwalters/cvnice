# BlinguaSDK


## Overview

### Available Operations

* [text_translate_wrapper_text_translate_target_lang_post](#text_translate_wrapper_text_translate_target_lang_post) - Text Translate Wrapper
* [detect_patterns_patterns_pattern_params_post](#detect_patterns_patterns_pattern_params_post) - Detect Patterns
* [text_replace_wrapper_text_replace_replacement_rules_post](#text_replace_wrapper_text_replace_replacement_rules_post) - Text Replace Wrapper
* [detect_ner_wrapper_text_detect_ner_ner_tags_post](#detect_ner_wrapper_text_detect_ner_ner_tags_post) - Detect Ner Wrapper
* [text_summarize_wrapper_text_summarize_summary_length_post](#text_summarize_wrapper_text_summarize_summary_length_post) - Text Summarize Wrapper
* [text_qna_wrapper_text_qna_question_post](#text_qna_wrapper_text_qna_question_post) - Text Qna Wrapper
* [text_intent_wrapper_text_intent_post](#text_intent_wrapper_text_intent_post) - Text Intent Wrapper
* [text_lemstem_wrapper_text_lemstem_operation_post](#text_lemstem_wrapper_text_lemstem_operation_post) - Text Lemstem Wrapper
* [text_tokenize_wrapper_text_tokenize_post](#text_tokenize_wrapper_text_tokenize_post) - Text Tokenize Wrapper
* [text_embed_wrapper_text_embed_task_type_post](#text_embed_wrapper_text_embed_task_type_post) - Text Embed Wrapper
* [text_generate_wrapper_text_generate_length_post](#text_generate_wrapper_text_generate_length_post) - Text Generate Wrapper
* [detect_spam_wrapper_text_detect_spam_post](#detect_spam_wrapper_text_detect_spam_post) - Detect Spam Wrapper
* [text_clean_wrapper_text_clean_post](#text_clean_wrapper_text_clean_post) - Text Clean Wrapper
* [text_normalize_wrapper_text_normalize_post](#text_normalize_wrapper_text_normalize_post) - Text Normalize Wrapper
* [text_spellcheck_wrapper_text_spellcheck_post](#text_spellcheck_wrapper_text_spellcheck_post) - Text Spellcheck Wrapper
* [text_srl_wrapper_text_srl_post](#text_srl_wrapper_text_srl_post) - Text Srl Wrapper
* [text_cluster_wrapper_text_cluster_post](#text_cluster_wrapper_text_cluster_post) - Text Cluster Wrapper
* [text_sentiment_wrapper_text_sentiment_post](#text_sentiment_wrapper_text_sentiment_post) - Text Sentiment Wrapper
* [text_topic_wrapper_text_topic_post](#text_topic_wrapper_text_topic_post) - Text Topic Wrapper
* [text_parts_of_speech_wrapper_text_parts_of_speech_post](#text_parts_of_speech_wrapper_text_parts_of_speech_post) - Text Parts Of Speech Wrapper
* [text_paraphrase_wrapper_text_paraphrase_post](#text_paraphrase_wrapper_text_paraphrase_post) - Text Paraphrase Wrapper
* [text_segment_wrapper_text_segment_post](#text_segment_wrapper_text_segment_post) - Text Segment Wrapper
* [text_badness_wrapper_text_toxic_analysis_type_post](#text_badness_wrapper_text_toxic_analysis_type_post) - Text Badness Wrapper
* [text_emojis_wrapper_text_replace_emojis_post](#text_emojis_wrapper_text_replace_emojis_post) - Text Emojis Wrapper
* [text_tfidf_wrapper_text_tfidf_post](#text_tfidf_wrapper_text_tfidf_post) - Text Tfidf Wrapper
* [text_idioms_wrapper_text_idioms_post](#text_idioms_wrapper_text_idioms_post) - Text Idioms Wrapper
* [text_sense_disambiguation_wrapper_text_sense_disambiguation_post](#text_sense_disambiguation_wrapper_text_sense_disambiguation_post) - Text Sense Disambiguation Wrapper
* [text_frequency_wrapper_text_frequency_post](#text_frequency_wrapper_text_frequency_post) - Text Frequency Wrapper
* [text_anomaly_wrapper_text_anomaly_post](#text_anomaly_wrapper_text_anomaly_post) - Text Anomaly Wrapper
* [text_core_reference_wrapper_text_core_reference_post](#text_core_reference_wrapper_text_core_reference_post) - Text Core Reference Wrapper

## text_translate_wrapper_text_translate_target_lang_post

translate the given text into the target language.

`Parameters`:
1. user_input (str): The input sentence to be translated.
Example: "The phone number is 123-456-7890."

2. target_lang (str): The target language for translation.
Example: "french".

`Returns`:
str: The translated text in the target language.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_translate_wrapper_text_translate_target_lang_post(target_lang='<value>', request_body='<value>', api_key='<value>')

if res.text_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `target_lang`      | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextTranslateWrapperTextTranslateTargetLangPostResponse](../../models/operations/texttranslatewrappertexttranslatetargetlangpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## detect_patterns_patterns_pattern_params_post

Extracts patterns from the given input sentence.

`Parameters`:
1. user_input (str): The input sentence containing information to be extracted.
Example: "The phone number is 123-456-7890."

2. patterns (str): Comma-separated patterns to be extracted.
Example: "email, name, phone number, address, date of birth".

`Returns`:
    list: A list containing the extracted patterns. If no pattern is found, returns None.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.detect_patterns_patterns_pattern_params_post(pattern_params='<value>', request_body='<value>', api_key='<value>')

if res.str_list_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `pattern_params`   | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.DetectPatternsPatternsPatternParamsPostResponse](../../models/operations/detectpatternspatternspatternparamspostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_replace_wrapper_text_replace_replacement_rules_post

Replace words in the original text according to the replacement rules provided.

Parameters:
1. user_input (str): The input sentence to be modified.
    Example: "I love Lamborghini, but Bugatti is even better. Although, Mercedes is a class above all."

2. replacement_rules (str): A detailed prompt specifying the replacement rules.
    Example: "all mentioned cars with mehran but mercerdes with toyota"

Returns:
str: The modified text with replacements.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_replace_wrapper_text_replace_replacement_rules_post(replacement_rules='<value>', request_body='<value>', api_key='<value>')

if res.text_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter           | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `replacement_rules` | *str*               | :heavy_check_mark:  | N/A                 |
| `request_body`      | *str*               | :heavy_check_mark:  | N/A                 |
| `api_key`           | *Optional[str]*     | :heavy_minus_sign:  | N/A                 |


### Response

**[operations.TextReplaceWrapperTextReplaceReplacementRulesPostResponse](../../models/operations/textreplacewrappertextreplacereplacementrulespostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## detect_ner_wrapper_text_detect_ner_ner_tags_post

Perform Named Entity Recognition (NER) detection on the input text.

Parameters:
1. user_input (str): The input sentence to be modified.
    Example: "I love Lamborghini, but Bugatti is even better. Although, Mercedes is a class above all."

2. ner_tags (str, optional): A comma-separated string specifying the NER tags.
    Example: "organization, date, time"
    Default: "person, location, organization, date, time, money, percent"

Returns:
list: A list of tuples containing the detected NER entities.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.detect_ner_wrapper_text_detect_ner_ner_tags_post(ner_tags='<value>', request_body='<value>', api_key='<value>')

if res.tuple_list_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `ner_tags`         | *Optional[str]*    | :heavy_check_mark: | N/A                |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.DetectNerWrapperTextDetectNerNerTagsPostResponse](../../models/operations/detectnerwrappertextdetectnernertagspostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_summarize_wrapper_text_summarize_summary_length_post

Generate a summary of the input text.

Parameters:
1. user_input (str): The input sentence to be summarized.
    Example: "I love Lamborghini, but Bugatti is even better"

2. summary_length (str, optional): The length of the summary.
    Values (str): "short", "medium" or "long"
    Default: "short"

Returns:
str: The generated summary.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_summarize_wrapper_text_summarize_summary_length_post(summary_length='<value>', request_body='<value>', api_key='<value>')

if res.text_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `summary_length`   | *Optional[str]*    | :heavy_check_mark: | N/A                |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextSummarizeWrapperTextSummarizeSummaryLengthPostResponse](../../models/operations/textsummarizewrappertextsummarizesummarylengthpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_qna_wrapper_text_qna_question_post

answer the given question based on the input text.

Parameters:
1. user_input (str): The input sentence on which the question is based.
    Example: "OpenAI has hosted a hackathon for developers to build AI models. The event took place on 15th October 2022."

2. question (str): question to be answered
    Example: "When did the event happen?"

Returns:
str: The generated summary.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_qna_wrapper_text_qna_question_post(question='<value>', request_body='<value>', api_key='<value>')

if res.text_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `question`         | *Optional[str]*    | :heavy_check_mark: | N/A                |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextQnaWrapperTextQnaQuestionPostResponse](../../models/operations/textqnawrappertextqnaquestionpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_intent_wrapper_text_intent_post

Identify the intent of the user input.

Parameters:
1. user_input (str): The input sentence of which the intent is to be identified.
    Example: "OpenAI has hosted a hackathon for developers to build AI models."

Returns:
str: The identified intent.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_intent_wrapper_text_intent_post(request_body='<value>', api_key='<value>')

if res.str_list_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextIntentWrapperTextIntentPostResponse](../../models/operations/textintentwrappertextintentpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_lemstem_wrapper_text_lemstem_operation_post

Text Lemstem Wrapper

### Example Usage

```python
import blinguasdk
from blinguasdk.models import components

s = blinguasdk.BlinguaSDK()


res = s.text_lemstem_wrapper_text_lemstem_operation_post(operation=components.LemStemOp.LEMMATIZATION, request_body='<value>', api_key='<value>')

if res.text_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `operation`                                                  | [components.LemStemOp](../../models/components/lemstemop.md) | :heavy_check_mark:                                           | N/A                                                          |
| `request_body`                                               | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `api_key`                                                    | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |


### Response

**[operations.TextLemstemWrapperTextLemstemOperationPostResponse](../../models/operations/textlemstemwrappertextlemstemoperationpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_tokenize_wrapper_text_tokenize_post

Text Tokenize Wrapper

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_tokenize_wrapper_text_tokenize_post(request_body='<value>', break_point=' ', api_key='<value>')

if res.str_list_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `break_point`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextTokenizeWrapperTextTokenizePostResponse](../../models/operations/texttokenizewrappertexttokenizepostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_embed_wrapper_text_embed_task_type_post

Perform stemming or lemmatization on the input text.

Parameters:
1. user_input (str): The input sentence to be processed.
    Example: "OpenAI has hosted a hackathon for developers to build AI models."

2. type (str, optional): The type of text processing to be performed.
    Values (str): "stemming" or "lemmatization"
    Default: "stemming"

Returns:
str: The processed sentence.

### Example Usage

```python
import blinguasdk
from blinguasdk.models import components

s = blinguasdk.BlinguaSDK()


res = s.text_embed_wrapper_text_embed_task_type_post(task_type=components.EmbedTaskType.CLUSTERING, request_body='<value>', api_key='<value>')

if res.optional_list_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `task_type`                                                          | [components.EmbedTaskType](../../models/components/embedtasktype.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `request_body`                                                       | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `api_key`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |


### Response

**[operations.TextEmbedWrapperTextEmbedTaskTypePostResponse](../../models/operations/textembedwrappertextembedtasktypepostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_generate_wrapper_text_generate_length_post

Generate text based on the input text.

Parameters:
1. user_input (str): The input sentence to generate text from.
    Example: "I love Lamborghini, but Bugatti is even better"

2. ans_length (str, optional): The length of the generated text.
    Values (str): "short", "medium" or "long"
    Default: "short"

Returns:
str: The generated text.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_generate_wrapper_text_generate_length_post(length='<value>', request_body='<value>', api_key='<value>')

if res.text_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `length`           | *Optional[str]*    | :heavy_check_mark: | N/A                |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextGenerateWrapperTextGenerateLengthPostResponse](../../models/operations/textgeneratewrappertextgeneratelengthpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## detect_spam_wrapper_text_detect_spam_post

Perform spam detection on the input text.

Parameters:
1. user_input (str): The input sentence to perform spam detection on.
    Example: "Congratulations! You have won a lottery of $1,000,000!"

2. num_classes (str, optional): The number of classes for spam detection.
    Default: "spam, not_spam, unknown"

3. explanation (bool, optional): Whether to include an explanation in the result.
    Default: True

Returns:
dict: A dictionary containing the prediction and explanation (if available).

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.detect_spam_wrapper_text_detect_spam_post(request_body='<value>', detect_classes='spam, not_spam, unknown', explain=True, api_key='<value>')

if res.dict_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `detect_classes`   | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `explain`          | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.DetectSpamWrapperTextDetectSpamPostResponse](../../models/operations/detectspamwrappertextdetectspampostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_clean_wrapper_text_clean_post

Clean the input text based on the given information.

Parameters:
1. user_input (str): The input sentence to be cleaned.
    Example:
    ```
    <h1>Heading</h1> <p>para</p> visit to this website https://www.google.com for more information
    ```

2. clean_info (str): The information on how to clean the text.
    Example: "remove h1 tags but keep their inner text and remove links and fullstop"

Returns:
str: The cleaned text.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_clean_wrapper_text_clean_post(clean_info='<value>', request_body='<value>', api_key='<value>')

if res.text_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `clean_info`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextCleanWrapperTextCleanPostResponse](../../models/operations/textcleanwrappertextcleanpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_normalize_wrapper_text_normalize_post

Transform user input to either uppercase or lowercase string.

Parameters:
1. user_input (str): The string to be transformed.

2. mode (str): The transformation mode. Valid values are 'uppercase' or 'lowercase'.
Default: "uppercase"

Returns:
str: The transformed string.

### Example Usage

```python
import blinguasdk
from blinguasdk.models import operations

s = blinguasdk.BlinguaSDK()


res = s.text_normalize_wrapper_text_normalize_post(request_body='<value>', mode=operations.Mode.UPPERCASE, api_key='<value>')

if res.text_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request_body`                                               | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `mode`                                                       | [Optional[operations.Mode]](../../models/operations/mode.md) | :heavy_minus_sign:                                           | N/A                                                          |
| `api_key`                                                    | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |


### Response

**[operations.TextNormalizeWrapperTextNormalizePostResponse](../../models/operations/textnormalizewrappertextnormalizepostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_spellcheck_wrapper_text_spellcheck_post

Correct the misspelled words in the input text.

Parameters:
1. user_input (str): The input sentence to perform spell correction on.
   Example: "we wlli oderr pzzia adn buregsr at nghti"

Returns:
str: The corrected version of the input sentence with all misspelled words replaced by their correct spellings.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_spellcheck_wrapper_text_spellcheck_post(request_body='<value>', api_key='<value>')

if res.text_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextSpellcheckWrapperTextSpellcheckPostResponse](../../models/operations/textspellcheckwrappertextspellcheckpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_srl_wrapper_text_srl_post

Perform Semantic Role Labeling (SRL) on the input text.

Parameters:
1. user_input (str): The input sentence to perform SRL on.
    Example: "John ate an apple."

Returns:
dict: A dictionary containing the detected SRL entities.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_srl_wrapper_text_srl_post(request_body='<value>', api_key='<value>')

if res.dict_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextSrlWrapperTextSrlPostResponse](../../models/operations/textsrlwrappertextsrlpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_cluster_wrapper_text_cluster_post

Cluster the sentences based on their similarity.

Parameters:
1. user_input (str): The input sentences to be clustered.
    Example: '''
    "sentence 1, sentence 2, sentence 3, ..."

Returns:
dict: A dictionary where each key-value pair represents a cluster.
    The key is the cluster number, and the value is a list containing similar sentences.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_cluster_wrapper_text_cluster_post(request_body='<value>', api_key='<value>')

if res.dict_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextClusterWrapperTextClusterPostResponse](../../models/operations/textclusterwrappertextclusterpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_sentiment_wrapper_text_sentiment_post

Perform sentiment detection on the input text.

Parameters:
1. user_input (str): The input sentence to perform sentiment detection on.
    Example: "Congratulations! You have won a lottery of $1,000,000!"

2. num_classes (str, optional): The number of categories for sentiment detection.
    Default: "positive, negative, neutral"

3. explanation (bool, optional): Whether to include an explanation in the result.
    Default: True

Returns:
dict: A dictionary containing the prediction and explanation (if available).

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_sentiment_wrapper_text_sentiment_post(request_body='<value>', num_classes='positive, negative, neutral', explanation=True, api_key='<value>')

if res.dict_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `num_classes`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `explanation`      | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextSentimentWrapperTextSentimentPostResponse](../../models/operations/textsentimentwrappertextsentimentpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_topic_wrapper_text_topic_post

Perform topic detection on the input text.

Parameters:
1. user_input (str): The input sentence to perform topic detection on.
    Example: "Congratulations! You have won a lottery of $1,000,000!"

2. num_classes (str, optional): The number of categories for topic detection.
    Default: "story, horror, comedy"

3. explanation (bool, optional): Whether to include an explanation in the result.
    Default: True

Returns:
dict: A dictionary containing the prediction and explanation (if available).

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_topic_wrapper_text_topic_post(num_classes='<value>', request_body='<value>', explanation=True, api_key='<value>')

if res.dict_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `num_classes`      | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `explanation`      | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextTopicWrapperTextTopicPostResponse](../../models/operations/texttopicwrappertexttopicpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_parts_of_speech_wrapper_text_parts_of_speech_post

Perform Part-of-Speech (POS) detection on the input text.

Parameters:
1. user_input (str): The input sentence to be analyzed.
    Example: "I love Lamborghini, but Bugatti is even better. Although, Mercedes is a class above all."

2. pos_tags (str, optional): A comma-separated string specifying the POS tags.
    Example: "noun, verb, adjective"
    Default: "More than 50 TAGS already defined"

default_pos_tags = 'noun, verb, adjective, adverb, pronoun, preposition, conjunction, interjection, determiner, cardinal, foreign, number, date, time, ordinal, money, percent, symbol, punctuation, emoticon, hashtag, email, url, mention, phone, ip, cashtag, entity, noun_phrase, verb_phrase, adjective_phrase, adverb_phrase, pronoun_phrase, preposition_phrase, conjunction_phrase, interjection_phrase, determiner_phrase, cardinal_phrase, foreign_phrase, number_phrase, date_phrase, time_phrase, ordinal_phrase, money_phrase, percent_phrase, symbol_phrase, punctuation_phrase, emoticon_phrase, hashtag_phrase, email_phrase, url_phrase, mention_phrase, phone_phrase, ip_phrase, cashtag_phrase, entity_phrase'

Returns:
list: A list of tuples containing the detected POS entities.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_parts_of_speech_wrapper_text_parts_of_speech_post(request_body='<value>', pos_tags='<value>', api_key='<value>')

if res.optional_list_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `pos_tags`         | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextPartsOfSpeechWrapperTextPartsOfSpeechPostResponse](../../models/operations/textpartsofspeechwrappertextpartsofspeechpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_paraphrase_wrapper_text_paraphrase_post

Determine if two sentences are paraphrases of each other.

Parameters:
1. user_input (list): A list containing two sentences to be checked for paraphrasing.
    Example: ["OpenAI has hosted a hackathon for developers.", "The event was a huge success with over 1000 participants."]

2. explanation (bool, optional): Whether to include an explanation in the result.
    Default: True

Returns:
str: The prediction of whether the sentences are paraphrases or not.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_paraphrase_wrapper_text_paraphrase_post(request_body=[
    '<value>',
], explanation=True, api_key='<value>')

if res.dict_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `request_body`     | List[*str*]        | :heavy_check_mark: | N/A                |
| `explanation`      | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextParaphraseWrapperTextParaphrasePostResponse](../../models/operations/textparaphrasewrappertextparaphrasepostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_segment_wrapper_text_segment_post

Segment the given text into individual sentences separated by full stops.

Parameters:
1. text_paragraph (str): The input text paragraph(s) to be segmented into sentences.
    Example: "The sun gently rose ..."

2. logical (bool, optional): Whether to logically segment the text into sentences.
    If True, the prompt code will be used. If False, the text will be split at full stops.
    Default: True

Returns:
list: A Python list of sentences.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_segment_wrapper_text_segment_post(request_body='<value>', logical=True, api_key='<value>')

if res.optional_list_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `logical`          | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextSegmentWrapperTextSegmentPostResponse](../../models/operations/textsegmentwrappertextsegmentpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_badness_wrapper_text_toxic_analysis_type_post

Check if the user input contains profanity, biased language, or sarcastic language based on the given analysis type and threshold.

Parameters:
1. user_input (str): The input text to be analyzed.

2. analysis_type (str): The type of analysis to be performed.
    Values (str): "profanity", "bias", "sarcasm"

3. threshold (str, optional): The threshold level for blocking the respective language.
    Values (str): "BLOCK_NONE", "BLOCK_ONLY_HIGH", "BLOCK_MEDIUM_AND_ABOVE", "BLOCK_LOW_AND_ABOVE"
    Default: "BLOCK_NONE"

Returns:
bool: True if the user input contains the respective language, False otherwise.

### Example Usage

```python
import blinguasdk
from blinguasdk.models import components, operations

s = blinguasdk.BlinguaSDK()


res = s.text_badness_wrapper_text_toxic_analysis_type_post(analysis_type=components.ToxicInputType.BIAS, request_body='<value>', threshold=operations.Threshold.BLOCK_NONE, api_key='<value>')

if res.bool_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `analysis_type`                                                        | [components.ToxicInputType](../../models/components/toxicinputtype.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `request_body`                                                         | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `threshold`                                                            | [Optional[operations.Threshold]](../../models/operations/threshold.md) | :heavy_minus_sign:                                                     | N/A                                                                    |
| `api_key`                                                              | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |


### Response

**[operations.TextBadnessWrapperTextToxicAnalysisTypePostResponse](../../models/operations/textbadnesswrappertexttoxicanalysistypepostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_emojis_wrapper_text_replace_emojis_post

Replace emojis with their meaning and full form in the given user input.

Parameters:
1. user_input (str): The input user input containing emojis.

Returns:
str: The user input with emojis replaced by their meaning and full form.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_emojis_wrapper_text_replace_emojis_post(request_body='<value>', api_key='<value>')

if res.text_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextEmojisWrapperTextReplaceEmojisPostResponse](../../models/operations/textemojiswrappertextreplaceemojispostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_tfidf_wrapper_text_tfidf_post

Calculate the TF-IDF matrix or unique n-grams for a given list of documents and n-gram size.

Parameters:
1. documents (list): A list of documents.

2. ngrams_size (int): The size of n-grams.

3. output_type (str): The type of output to be generated. Values can be "tfidf", "ngrams", or "all".

Returns:
tuple: A tuple containing the TF-IDF matrix, the set of unique n-grams, or both based on the output_type.

### Example Usage

```python
import blinguasdk
from blinguasdk.models import components

s = blinguasdk.BlinguaSDK()


res = s.text_tfidf_wrapper_text_tfidf_post(ngram_size=907407, output_type=components.TFIDFOutputType.NGRAMS, request_body=[
    '<value>',
], api_key='<value>')

if res.tuple_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `ngram_size`                                                             | *int*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `output_type`                                                            | [components.TFIDFOutputType](../../models/components/tfidfoutputtype.md) | :heavy_check_mark:                                                       | N/A                                                                      |
| `request_body`                                                           | List[*str*]                                                              | :heavy_check_mark:                                                       | N/A                                                                      |
| `api_key`                                                                | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | N/A                                                                      |


### Response

**[operations.TextTfidfWrapperTextTfidfPostResponse](../../models/operations/texttfidfwrappertexttfidfpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_idioms_wrapper_text_idioms_post

Identify and extract any idioms present in the given sentence.

Parameters:
1. user_input (str): The input sentence.

Returns:
list: A list of extracted idioms. If no idiom is found, returns None.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()

req = '<value>'

res = s.text_idioms_wrapper_text_idioms_post(req)

if res.optional_list_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [str](../../models/.md)                    | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.TextIdiomsWrapperTextIdiomsPostResponse](../../models/operations/textidiomswrappertextidiomspostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_sense_disambiguation_wrapper_text_sense_disambiguation_post

Perform word sense disambiguation for a given input sentence and word to disambiguate.

Parameters:
1. user_input (str): The input sentence.

2. word_to_disambiguate (str): The word to disambiguate.

Returns:
list: A list of meanings and their explanations based on the context in the input sentence.
If the word does not appear in the input sentence, returns None.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_sense_disambiguation_wrapper_text_sense_disambiguation_post(word_to_disambiguate='<value>', request_body='<value>', api_key='<value>')

if res.optional_list_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter              | Type                   | Required               | Description            |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `word_to_disambiguate` | *str*                  | :heavy_check_mark:     | N/A                    |
| `request_body`         | *str*                  | :heavy_check_mark:     | N/A                    |
| `api_key`              | *Optional[str]*        | :heavy_minus_sign:     | N/A                    |


### Response

**[operations.TextSenseDisambiguationWrapperTextSenseDisambiguationPostResponse](../../models/operations/textsensedisambiguationwrappertextsensedisambiguationpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_frequency_wrapper_text_frequency_post

Calculate the frequency of specific words or all words in the given user input.

Parameters:
1. user_input (str): The input user input.

2. words (list, optional): The list of words to calculate the frequency for.
If None is provided, the function will calculate the frequency for all words.
Default: None

Returns:
dict: A dictionary where the key is the word and the value is its frequency.

### Example Usage

```python
import blinguasdk
from blinguasdk.models import components

s = blinguasdk.BlinguaSDK()


res = s.text_frequency_wrapper_text_frequency_post(body_text_frequency_wrapper_text_frequency_post=components.BodyTextFrequencyWrapperTextFrequencyPost(
    user_input='<value>',
), api_key='<value>')

if res.dict_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `body_text_frequency_wrapper_text_frequency_post`                                                                            | [components.BodyTextFrequencyWrapperTextFrequencyPost](../../models/components/bodytextfrequencywrappertextfrequencypost.md) | :heavy_check_mark:                                                                                                           | N/A                                                                                                                          |
| `api_key`                                                                                                                    | *Optional[str]*                                                                                                              | :heavy_minus_sign:                                                                                                           | N/A                                                                                                                          |


### Response

**[operations.TextFrequencyWrapperTextFrequencyPostResponse](../../models/operations/textfrequencywrappertextfrequencypostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_anomaly_wrapper_text_anomaly_post

Detect any anomalies or outliers in the given input text.

Parameters:
1. user_input (str): The input text to be analyzed.

Returns:
list: A list of detected anomalies with explanations of how they are anomalous.
If no anomalies are found, returns None.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_anomaly_wrapper_text_anomaly_post(request_body='<value>', api_key='<value>')

if res.optional_list_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextAnomalyWrapperTextAnomalyPostResponse](../../models/operations/textanomalywrappertextanomalypostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## text_core_reference_wrapper_text_core_reference_post

Perform coreference resolution on the given text to identify who (pronoun) refers to what/whom.

Parameters:
1. user_input (str): The input text to perform coreference resolution on.

Returns:
list: A list of resolved coreferences in the format "Pronoun refers to Entity".
If no pronouns are found or if the resolved references cannot be determined, returns None.

### Example Usage

```python
import blinguasdk

s = blinguasdk.BlinguaSDK()


res = s.text_core_reference_wrapper_text_core_reference_post(request_body='<value>', api_key='<value>')

if res.optional_list_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.TextCoreReferenceWrapperTextCoreReferencePostResponse](../../models/operations/textcorereferencewrappertextcorereferencepostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |
