from google.cloud import translate_v2 as translate
from app.settings import settings   # noqa

from app.scheme.transdata import TranslateResponse, TranslateRquest

translate_client = translate.Client()


def get_translate(
    input_: TranslateRquest, translate_client: translate.Client = translate_client
) -> TranslateResponse:
    """Translates a word or phrase.

    - clears spaces before and after
    - The specified input and input languages cannot be the same
    - if the recognized language does not match the specified input - an exception is thrown
    for the function to work correctly, it is necessary to set the GOOGLE_APPLICATION_CREDENTIALS
    environment variable containing the path to the file with credentials
    (the file must be available at this path)
    """
    result = translate_client.translate(input_.line, target_language=input_.out_lang)
    if result["detectedSourceLanguage"] != input_.in_lang:
        raise ValueError(
            f"Original message language recognized as \
                {result['detectedSourceLanguage']} while {input_.in_lang} is specified"
        )
    return TranslateResponse(
        input_line=input_.line,
        detected_input_lag=result["detectedSourceLanguage"],
        translaled_line=result["translatedText"],
    )
