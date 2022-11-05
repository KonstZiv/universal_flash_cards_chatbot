import pytest
from pydantic import ValidationError

from app.base_function.translator import get_translate
from app.scheme.transdata import ISO639_1, TranslateRequest
from app.settings import settings   # noqa


def test_get_translate():
    request_1 = TranslateRequest(
        in_lang=ISO639_1.English, out_lang=ISO639_1.Ukranian, line="makes"
    )

    request_2 = TranslateRequest(
        in_lang=ISO639_1.Russian, out_lang=ISO639_1.Ukranian, line="унылая пора"
    )

    request_3 = TranslateRequest(
        in_lang=ISO639_1.English, out_lang=ISO639_1.Ukranian, line="    assemble  "
    )

    assert get_translate(input_=request_1).translaled_line == "робить"

    assert get_translate(input_=request_2).translaled_line == "похмура пора"

    assert get_translate(input_=request_3).translaled_line == "зібрати"


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
