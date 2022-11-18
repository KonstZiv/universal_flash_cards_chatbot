from google.cloud import translate_v2 as translate
from scheme.transdata import TranslateRequest, TranslateResponse

# noqa !!!used to load the environment variables required for the function get_translateimporta
from settings import settings

translate_client = translate.Client()


def get_translate(
    input_: TranslateRequest, translate_client: translate.Client = translate_client
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
            "Original message language recognized as "
            f"{result['detectedSourceLanguage']} while {input_.in_lang} is specified"
        )
    return TranslateResponse(
        input_line=input_.line,
        translated_line=result["translatedText"],
    )
