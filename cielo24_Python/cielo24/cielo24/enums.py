# encoding: utf-8
from enum import Enum


class StrEnum(Enum):
    def __str__(self):
        return str(self.value)


class TaskType(StrEnum):
    JOB_CREATED = "JOB_CREATED"
    JOB_DELETED = "JOB_DELETED"
    JOB_ADD_MEDIA = "JOB_ADD_MEDIA"
    JOB_ADD_TRANSCRIPT = "JOB_ADD_TRANSCRIPT"
    JOB_PERFORM_TRANSCRIPTION = "JOB_PERFORM_TRANSCRIPTION"
    JOB_PERFORM_PREMIUM_SYNC = "JOB_PERFORM_PREMIUM_SYNC"
    JOB_UPDATE_ELEMENTLIST = "JOB_UPDATE_ELEMENTLIST"
    JOB_GET_TRANSCRIPT = "JOB_GET_TRANSCRIPT"
    JOB_GET_CAPTION = "JOB_GET_CAPTION"
    JOB_GET_ELEMENTLIST = "JOB_GET_ELEMENTLIST"


class ErrorType(StrEnum):
    LOGIN_INVALID = "LOGIN_INVALID"
    ACCOUNT_EXISTS = "ACCOUNT_EXISTS"
    ACCOUNT_DOES_NOT_EXIST = "ACCOUNT_DOES_NOT_EXIST"
    ACCOUNT_UNPRIVILEGED = "ACCOUNT_UNPRIVILEGED"
    BAD_API_TOKEN = "BAD_API_TOKEN"
    INVALID_QUERY = "INVALID_QUERY"
    INVALID_OPTION = "INVALID_OPTION"
    INVALID_URL = "INVALID_URL"
    MISSING_PARAMETER = "MISSING_PARAMETER"
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    ITEM_NOT_FOUND = "ITEM_NOT_FOUND"
    INVALID_RETURN_HANDLERS = "INVALID_RETURN_HANDLERS"
    NOT_PARENT_ACCOUNT = "NOT_PARENT_ACCOUNT"
    NO_CHILDREN_FOUND = "NO_CHILDREN_FOUND"
    UNHANDLED_ERROR = "UNHANDLED_ERROR"
  

class JobStatus(StrEnum):
    AUTHORIZING = "Authorizing"
    PENDING = "Pending"
    IN_PROCESS = "In Process"
    COMPLETE = "Complete"
    MEDIA_FAILURE = "Media Failure"
    REVIEWING = "Reviewing"
  

class TaskStatus(StrEnum):
    COMPLETE = "COMPLETE"
    INPROGRESS = "INPROGRESS"
    ABORTED = "ABORTED"
    FAILED = "FAILED"
  

class Priority(StrEnum):
    ECONOMY = "ECONOMY"
    STANDARD = "STANDARD"
    PRIORITY = "PRIORITY"
    CRITICAL = "CRITICAL"
  

class Fidelity(StrEnum):
    MECHANICAL = "MECHANICAL"
    PREMIUM = "PREMIUM"
    PROFESSIONAL = "PROFESSIONAL"
  

class CaptionFormat(StrEnum):
    SRT = "SRT"
    SBV = "SBV"
    SCC = "SCC"
    DFXP = "DFXP"
    QT = "QT"
    TRANSCRIPT = "TRANSCRIPT"
    TWX = "TWX"
    TPM = "TPM"
    WEB_VTT = "WEB_VTT"
    ECHO = "ECHO"


class TokenType(StrEnum):
    WORD = "word"
    PUNCTUATION = "punctuation"
    SOUND = "sound"
  

class Tag(StrEnum):
    UNKNOWN = "UNKNOWN"
    INAUDIBLE = "INAUDIBLE"
    CROSSTALK = "CROSSTALK"
    MUSIC = "MUSIC"
    NOISE = "NOISE"
    LAUGH = "LAUGH"
    COUGH = "COUGH"
    FOREIGN = "FOREIGN"
    BLANK_AUDIO = "BLANK_AUDIO"
    APPLAUSE = "APPLAUSE"
    BLEEP = "BLEEP"
    ENDS_SENTENCE = "ENDS_SENTENCE"
  

class SpeakerId(StrEnum):
    NO = "no"
    NUMBER = "number"
    NAME = "name"
  

class SpeakerGender(StrEnum):
    UNKNOWN = "UNKNOWN"
    MALE = "MALE"
    FEMALE = "FEMALE"
  

class Case(StrEnum):
    UPPER = "upper"
    LOWER = "lower"
    UNCHANGED = ""
  

class LineEnding(StrEnum):
    UNIX = "UNIX"
    WINDOWS = "WINDOWS"
    OSX = "OSX"


class CustomerApprovalSteps(StrEnum):
    TRANSLATION = "TRANSLATION"
    RETURN = "RETURN"
  

class CustomerApprovalTools(StrEnum):
    AMARA = "AMARA"
    CIELO24 = "CIELO24"
  

class Language(StrEnum):
    English = "en"
    French = "fr"
    Spanish = "es"
    German = "de"
    Mandarin_Chinese = "cmn"
    Portuguese = "pt"
    Japanese = "jp"
    Arabic = "ar"
    Korean = "ko"
    Traditional_Chinese = "zh"
    Hindi = "hi"
    Italian = "it"
    Russian = "ru"
    Turkish = "tr"
    Hebrew = "he"


class IWP(StrEnum):
    PREMIUM = "PREMIUM"
    INTERIM_PROFESSIONAL = "INTERIM_PROFESSIONAL"
    PROFESSIONAL = "PROFESSIONAL"
    SPEAKER_ID = "SPEAKER_ID"
    FINAL = "FINAL"
    MECHANICAL = "MECHANICAL"
    CUSTOMER_APPROVED_RETURN = "CUSTOMER_APPROVED_RETURN"
    CUSTOMER_APPROVED_TRANSLATION = "CUSTOMER_APPROVED_TRANSLATION"

class JobDifficulty(StrEnum):
    GOOD = "Good"
    BAD = "Bad"
    UNKNOWN = "Unknown"
