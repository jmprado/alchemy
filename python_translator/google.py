import json
import requests

import environment


class Translator:
    """ Google class to do the translation based on the following properties: \n
    - q (text to be translated), \n
    - source (language from) code, \n
    - target (language to) code. \n
    To find the supported languages and their codes visit https://cloud.google.com/translate/docs/languages.
    """
    __f = open('supported_languages.json')
    __supported_languages = json.load(__f)

    def __init__(self, q, source, target):
        self.q = q
        self.source = source
        self.target = target
        self.__validate_text_length()
        self.__verify_language_support()

    def do_translation(self):
        """ Translate and print the text from class properties q (text to be translated), source (language from)
        , target (language to) """
        translated_text = self.__do_translation_request()
        self.__print_translation(translated_text)

    def __do_translation_request(self):
        """ Create and do the request to the Google Translator API """
        url_base = 'https://translation.googleapis.com/language/translate/v2?key='
        key = environment.api_key
        url = f'{url_base}{key}'
        body = {'q': self.q, 'source': self.source, 'target': self.target}
        try:
            r = requests.post(url, json=body)
            json_data = json.loads(r.text)
            translation_result = json_data['data']['translations'][0]['translatedText']
            return translation_result
        except requests.exceptions.RequestException as e:
            SystemExit(e)

    def __print_translation(self, text):
        """ Pretty print the translated text """
        language_source = self.__get_language_name(self.source)
        language_target = self.__get_language_name(self.target)
        print('------------------------------------------------')
        print(f'{language_source} -> {language_target}: \n{text}\n\n')

    def __get_language_name(self, language_code):
        """ Find language name from supported language list given language code """
        for language in self.__supported_languages['languages']:
            if language['code'] == language_code:
                return language['language']

        return 'Language not found'

    # Validation section
    def __validate_text_length(self):
        """ Validate the text length  """
        if len(self.q) == 0 or len(self.q) > 255:
            exit("The text to be translated is required and cannot have more than 255 characters.")

    def __verify_language_support(self):
        """ Verify it the languages inputted are supported """
        has_error = False
        str_error = ''
        if not self.__is_language_supported(self.source):
            str_error = "\nLanguage code 'from' not found in supported languages.\n"
            has_error = True
        if not self.__is_language_supported(self.target):
            str_error += "Language code 'to' not found in supported languages.\n"
            has_error = True
        if has_error:
            print('Visit https://cloud.google.com/translate/docs/languages to find the language codes.')
            exit(str_error)

    def __is_language_supported(self, language_code):
        """ Return True if the language code inputted is supported """
        for language in self.__supported_languages['languages']:
            if language['code'] == language_code:
                return True
        return False
