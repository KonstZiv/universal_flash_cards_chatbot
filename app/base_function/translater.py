from google.cloud import translate_v2 as translate
from settings import settings
from scheme.trans import TranslateRquest, TranslateResponse

translate_client = translate.Client()

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(f"Text: {result['input']}")
    print(f"Translation: {result['translatedText']}")
    print(f"Detected source language: {result['detectedSourceLanguage']}")


def get_translate(
    input_: TranslateRquest,
    translate_client: translate.Client = translate_client
) -> TranslateResponse:
    result = translate_client.translate(input_.line, target_language=input_.out_lang)
    if result["detectedSourceLanguage"] != input_.in_lang:
        raise ValueError(f"Original message language recognized as {result['detectedSourceLanguage']} while {input_.in_lang} is specified")
    return TranslateResponse(
        input_line=input_.line,
        detected_input_lag=result["detectedSourceLanguage"],
        translaled_line=result["translatedText"]
    )



if __name__ == "__main__":
    target = "uk"
    text = input("enter text: ")
    while text:
        translate_text(target=target, text=text)
        text = input("\nenter text: ")