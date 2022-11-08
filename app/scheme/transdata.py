from enum import Enum

from pydantic import BaseModel, validator


class ISO639_1(str, Enum):
    """Describes allowed languages in terms of ISO 639-1

    https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    """

    Abkhasian = "ab"
    Afar = "aa"
    Afrikaans = "af"
    Akan = "ak"
    Albanian = "sq"
    Amharic = "am"
    Arabic = "ar"
    Aragonese = "an"
    Armenian = "hy"
    Assamese = "as"
    Avaric = "av"
    Avestan = "ae"
    Aymara = "ay"
    Azerbaijani = "az"
    Bambara = "bm"
    Bashkir = "ba"
    Basque = "eu"
    Belarusian = "be"
    Bengali = "bn"
    Bislama = "bi"
    Bosnian = "bs"
    Breton = "br"
    Bulgarian = "bg"
    Burmese = "my"
    Catalan = "ca"
    Valencian = "ca"
    Chamorro = "ch"
    Chechen = "ce"
    Chichewa = "ny"
    Chewa = "ny"
    Nyanja = "ny"
    Chinese = "zh"
    ChurchSlavonic = "cu"
    OldSlavonic = "cu"
    OldChurchSlavonic = "cu"
    Chuvash = "cv"
    Cornish = "kw"
    Corsican = "co"
    Cree = "cr"
    Croatian = "hr"
    Czech = "cs"
    Danish = "da"
    Divehi = "dv"
    Dhivehi = "dv"
    Maldivian = "dv"
    Dutch = "nl"
    Flemish = "nl"
    Dzongkha = "dz"
    English = "en"
    Esperanto = "eo"
    Estonian = "et"
    Ewe = "ee"
    Faroese = "fo"
    Fijian = "fj"
    Finnish = "fi"
    French = "fr"
    WesternFrisian = "fy"
    Fulah = "ff"
    Gaelic = "gd"
    ScottishGaelic = "gd"
    Galician = "gl"
    Ganda = "lg"
    Georgian = "ka"
    German = "de"
    Greek = "el"
    Kalaallisut = "kl"
    Greenlandic = "kl"
    Guarani = "gn"
    Gujatati = "gu"
    Haitian = "ht"
    HaitianCreole = "ht"
    Hausa = "ha"
    Herbew = "he"
    Herero = "hz"
    Hindi = "hi"
    HiriMotu = "ho"
    Hungarian = "hu"
    Icelandic = "is"
    Ido = "io"
    Igbo = "ig"
    Indonesian = "id"
    Interlingua = "ia"
    Interlingue = "ie"
    Occidental = "ie"
    Inuktitut = "iu"
    Inupiaq = "ik"
    Irish = "ga"
    Italian = "it"
    Japanese = "ja"
    Javanese = "jv"
    Kannada = "kn"
    Kanuri = "kr"
    Kashmiri = "ks"
    Kazakh = "kk"
    CentralKhmer = "km"
    Kikuyu = "ki"
    Gikuyu = "ki"
    Kinyarwanda = "rw"
    Kirghiz = "ky"
    Kyrgyz = "ky"
    Komi = "kv"
    Kongo = "kg"
    Korean = "ko"
    Kuanyama = "kj"
    Kwanyama = "kj"
    Kurdish = "ku"
    Lao = "lo"
    Latin = "la"
    Latvian = "lv"
    Limburgan = "li"
    Limburger = "li"
    Limburgish = "li"
    Lingala = "ln"
    Lithuanian = "lt"
    LubaKatanga = "lu"
    Luxembourgish = "lb"
    Letzeburgesch = "lb"
    Macedonian = "mk"
    Malagasy = "mg"
    Malay = "ms"
    Malayalam = "ml"
    Maltese = "mt"
    Manx = "gv"
    Maori = "mi"
    Marathi = "mr"
    Marshallese = "mh"
    Mongolian = "mn"
    Nauru = "na"
    Navajo = "nv"
    Navaho = "nv"
    NorthNdebele = "nd"
    SouthNdebele = "nr"
    Ndonga = "ng"
    Nepali = "ne"
    Norwegian = "no"
    NorwegianBokmal = "nb"
    NorwegianNynorsk = "nn"
    SichuanYi = "ii"
    Nuosu = "ii"
    Occitan = "oc"
    Ojibwa = "oj"
    Oriya = "or"
    Oromo = "om"
    Ossetian = "os"
    Ossetic = "os"
    Pali = "pi"
    Pashto = "ps"
    Pushto = "ps"
    Persian = "fa"
    Polish = "pl"
    Portuguese = "pt"
    Punjabi = "pa"
    Panjabi = "pa"
    Quechua = "qu"
    Romanian = "ro"
    Moldavian = "ro"
    Moldovan = "ro"
    Romanish = "rm"
    Rundi = "rn"
    Russian = "ru"
    NorthernSami = "se"
    Samoan = "sm"
    Sango = "sg"
    Sanskrit = "sa"
    Sardinian = "sc"
    Serbian = "sr"
    Shona = "sn"
    Sindhi = "sd"
    Sinhala = "si"
    Sinhalese = "si"
    Slovak = "sk"
    Slovenian = "sl"
    Somali = "so"
    SouthernSotho = "st"
    Spanish = "es"
    Castilian = "es"
    Sundanese = "su"
    Swahili = "sw"
    Swati = "ss"
    Swedish = "sv"
    Tagalog = "tl"
    Tahitian = "ty"
    Tajik = "tg"
    Tamil = "ta"
    Tatar = "tt"
    Telugu = "te"
    Thai = "th"
    Tibetan = "bo"
    Tigrinya = "ti"
    Tonga = "to"
    Tsonga = "ts"
    Tswanga = "tn"
    Turkish = "tr"
    Turkmen = "tk"
    Twi = "tw"
    Uighur = "ug"
    Uyghur = "ug"
    Ukranian = "uk"
    Urdu = "ur"
    Uzbek = "uz"
    Venda = "ve"
    Vietnamese = "vi"
    Volapuk = "vo"
    Walloon = "wa"
    Welsh = "cy"
    Wolof = "wo"
    Xhosa = "xh"
    Yiddish = "yi"
    Yoruba = "yo"
    Zhuang = "za"
    Chuang = "za"
    Zulu = "zu"


class TranslateRequest(BaseModel):
    """Describes data model for the translation request."""

    in_lang: ISO639_1
    out_lang: ISO639_1
    line: str

    @validator("out_lang")
    def out_lang_must_not_be_equal_in_lang(cls, out_lang, values):
        if out_lang == values["in_lang"]:
            raise ValueError("out_lang must not be equal to in_lang")
        return out_lang

    @validator("line")
    def prepare_line(cls, line):
        """Strip spaces before and after, convert to lowercase."""
        return line.strip().lower()


class TranslateResponse(BaseModel):
    """Describes data model for the translation response."""

    input_line: str
    translated_line: str
