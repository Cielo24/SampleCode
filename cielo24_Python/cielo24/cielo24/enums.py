# encoding: utf-8
from enum import Enum


class StrEnum(Enum):
    def __str__(self):
        return str(self.value)

    @classmethod
    def str_list(cls):
        return [str(x) for x in list(cls)]


class ErrorType(StrEnum):
    LOGIN_INVALID = 'LOGIN_INVALID'
    ACCOUNT_EXISTS = 'ACCOUNT_EXISTS'
    ACCOUNT_DOES_NOT_EXIST = 'ACCOUNT_DOES_NOT_EXIST'
    ACCOUNT_UNPRIVILEGED = 'ACCOUNT_UNPRIVILEGED'
    BAD_API_TOKEN = 'BAD_API_TOKEN'
    INVALID_QUERY = 'INVALID_QUERY'
    INVALID_OPTION = 'INVALID_OPTION'
    INVALID_URL = 'INVALID_URL'
    MISSING_PARAMETER = 'MISSING_PARAMETER'
    NOT_IMPLEMENTED = 'NOT_IMPLEMENTED'
    ITEM_NOT_FOUND = 'ITEM_NOT_FOUND'
    INVALID_RETURN_HANDLERS = 'INVALID_RETURN_HANDLERS'
    NOT_PARENT_ACCOUNT = 'NOT_PARENT_ACCOUNT'
    NO_CHILDREN_FOUND = 'NO_CHILDREN_FOUND'
    UNHANDLED_ERROR = 'UNHANDLED_ERROR'
  

class JobStatus(StrEnum):
    AUTHORIZING = 'Authorizing'
    PENDING = 'Pending'
    IN_PROCESS = 'In Process'
    COMPLETE = 'Complete'
    MEDIA_FAILURE = 'Media Failure'
    REVIEWING = 'Reviewing'
  

class Priority(StrEnum):
    ECONOMY = 'ECONOMY'
    STANDARD = 'STANDARD'
    PRIORITY = 'PRIORITY'
    CRITICAL = 'CRITICAL'
  

class Fidelity(StrEnum):
    MECHANICAL = 'MECHANICAL'
    PREMIUM = 'PREMIUM'
    PROFESSIONAL = 'PROFESSIONAL'
  

class CaptionFormat(StrEnum):
    SRT = 'SRT'
    SBV = 'SBV'
    SCC = 'SCC'
    DFXP = 'DFXP'
    QT = 'QT'
    TRANSCRIPT = 'TRANSCRIPT'
    TWX = 'TWX'
    TPM = 'TPM'
    WEB_VTT = 'WEB_VTT'
    ECHO = 'ECHO'


class TokenType(StrEnum):
    WORD = 'word'
    PUNCTUATION = 'punctuation'
    SOUND = 'sound'
  

class SoundTag(StrEnum):
    UNKNOWN = 'UNKNOWN'
    INAUDIBLE = 'INAUDIBLE'
    CROSSTALK = 'CROSSTALK'
    MUSIC = 'MUSIC'
    NOISE = 'NOISE'
    LAUGH = 'LAUGH'
    COUGH = 'COUGH'
    FOREIGN = 'FOREIGN'
    BLANK_AUDIO = 'BLANK_AUDIO'
    APPLAUSE = 'APPLAUSE'
    BLEEP = 'BLEEP'
    ENDS_SENTENCE = 'ENDS_SENTENCE'
  

class SpeakerId(StrEnum):
    NO = 'no'
    NUMBER = 'number'
    NAME = 'name'
  

class SpeakerGender(StrEnum):
    UNKNOWN = 'UNKNOWN'
    MALE = 'MALE'
    FEMALE = 'FEMALE'
  

class Case(StrEnum):
    UPPER = 'upper'
    LOWER = 'lower'
    UNCHANGED = ''
  

class LineEnding(StrEnum):
    UNIX = 'UNIX'
    WINDOWS = 'WINDOWS'
    OSX = 'OSX'


class CustomerApprovalStep(StrEnum):
    TRANSLATION = 'TRANSLATION'
    RETURN = 'RETURN'
  

class CustomerApprovalTool(StrEnum):
    AMARA = 'AMARA'
    CIELO24 = 'CIELO24'
  

class Language(StrEnum):
    ENGLISH = 'en'
    FRENCH = 'fr'
    SPANISH = 'es'
    GERMAN = 'de'
    MANDARIN_CHINESE = 'cmn'
    PORTUGUESE = 'pt'
    JAPANESE = 'jp'
    ARABIC = 'ar'
    KOREAN = 'ko'
    TRADITIONAL_CHINESE= 'zh'
    HINDI = 'hi'
    ITALIAN = 'it'
    RUSSIAN = 'ru'
    TURKISH = 'tr'
    HEBREW = 'he'


class IWP(StrEnum):
    PREMIUM = 'PREMIUM'
    INTERIM_PROFESSIONAL = 'INTERIM_PROFESSIONAL'
    PROFESSIONAL = 'PROFESSIONAL'
    SPEAKER_ID = 'SPEAKER_ID'
    FINAL = 'FINAL'
    MECHANICAL = 'MECHANICAL'
    CUSTOMER_APPROVED_RETURN = 'CUSTOMER_APPROVED_RETURN'
    CUSTOMER_APPROVED_TRANSLATION = 'CUSTOMER_APPROVED_TRANSLATION'


class JobDifficulty(StrEnum):
    GOOD = 'Good'
    BAD = 'Bad'
    UNKNOWN = 'Unknown'
