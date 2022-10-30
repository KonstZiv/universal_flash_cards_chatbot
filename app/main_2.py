from settings import settings
from lib.translater import get_translate
from scheme.trans import TranslateResponse, TranslateRquest, ISO639_1


input_data = TranslateRquest(
    in_lang=ISO639_1.English,
    out_lang=ISO639_1.Ukranian,
    line=""
)

while True:
    line = input("input line: ")
    if not line:
        break
    input_data.line = line
    result = get_translate(
        input_=input_data
    )
    print(f"result: {result.translaled_line}")

