from unittest.mock import patch

import pytest
from pydantic import ValidationError

from app.base_function.translator import get_translate, translate_client
from app.scheme.transdata import ISO639_1, TranslateRequest
# used to load the environment variables required for the function get_translate
from app.settings import settings  # noqa !!!


@pytest.mark.parametrize(
    ("translate_request", "mock_translate_return_value", "right_answer"),
    (
        (
            TranslateRequest(
                in_lang=ISO639_1.English, out_lang=ISO639_1.Ukrainian, line="makes"
            ),
            {
                "translatedText": "робить",
                "detectedSourceLanguage": "en",
                "input": "makes",
            },
            "робить",
        ),
        (
            TranslateRequest(
                in_lang=ISO639_1.Russian, out_lang=ISO639_1.Ukrainian, line="унылая пора"
            ),
            {
                "translatedText": "похмура пора",
                "detectedSourceLanguage": "ru",
                "input": "унылая пора",
            },
            "похмура пора",
        ),
        (
            TranslateRequest(
                in_lang=ISO639_1.English,
                out_lang=ISO639_1.Ukrainian,
                line="    assemble  ",
            ),
            {
                "translatedText": "зібрати",
                "detectedSourceLanguage": "en",
                "input": "assemble",
            },
            "зібрати",
        ),
    ),
)
def test_get_translate(translate_request, mock_translate_return_value, right_answer):

    with patch.object(
        translate_client, "translate", return_value=mock_translate_return_value
    ) as mock_translate:
        assert get_translate(input_=translate_request).translated_line == right_answer

    mock_translate.assert_called_once_with(
        translate_request.line, target_language=translate_request.out_lang
    )


def test_validate_in_data():
    with pytest.raises(ValidationError) as exc_info:
        TranslateRequest(
            in_lang=ISO639_1.English, out_lang=ISO639_1.English, line="    assemble  "
        )
    assert exc_info.value.errors() == [
        {
            "loc": ("out_lang",),
            "msg": "out_lang must not be equal to in_lang",
            "type": "value_error",
        }
    ]


def test_matching_indicated_and_recognized_lang():
    translate_request = TranslateRequest(
        in_lang=ISO639_1.Haitian, out_lang=ISO639_1.Ukrainian, line="    assemble  "
    )
    mock_translate_return_value = {
        "translatedText": "зібрати",
        "detectedSourceLanguage": "en",
        "input": "assemble",
    }

    with patch.object(
        translate_client, "translate", return_value=mock_translate_return_value
    ) as mock_translate:
        with pytest.raises(ValueError) as exc_info:
            get_translate(input_=translate_request)
        assert "Original message language recognized as" in str(exc_info.value)

    mock_translate.assert_called_once_with(
        translate_request.line, target_language=translate_request.out_lang
    )
