from app.settings import settings   # noqa !!!used to load the environment variables required for the function get_translate
import pytest
from pydantic import ValidationError
from unittest.mock import patch
from app.base_function.translator import translate_client

from app.base_function.translator import get_translate
from app.scheme.transdata import ISO639_1, TranslateRequest


def test_get_translate():
    request_1 = TranslateRequest(
        in_lang=ISO639_1.English, out_lang=ISO639_1.Ukranian, line="makes"
    )

    with patch.object(translate_client, "translate", return_value="робить") as mock_translate:
        assert get_translate(input_=request_1).translated_line == "робить"

        mock_translate.assert_called_once_with(request_1.line, target_language=request_1.out_lang)


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
    request_5 = TranslateRequest(
        in_lang=ISO639_1.Haitian, out_lang=ISO639_1.Ukranian, line="    assemble  "
    )
    with pytest.raises(ValueError) as exc_info:
        get_translate(input_=request_5)
    assert "Original message language recognized as" in str(exc_info.value)
