from ibm_watson import LanguageTranslatorV


url_lt='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/1529bb61-9cd8-4af6-a1dd-b73d4d758e70'
apikey_lt='lPS5ySK9ZQCbydHrlyri3gTLeX1d1lRCaIZuhSbYFLRN'
version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator
from pandas.io.json import json_normalize

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
translation_response

translation=translation_response.get_result()
translation

spanish_translation =translation['translations'][0]['translation']
spanish_translation

translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()
translation_eng=translation_new['translations'][0]['translation']
translation_eng

French_translation=language_translator.translate(
    text=translation_eng , model_id='en-fr').get_result()

French_translation['translations'][0]['translation']
