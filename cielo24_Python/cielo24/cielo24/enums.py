# encoding: utf-8
class TaskType(object):
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


class ErrorType(object):
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
  

class JobStatus(object):
    Authorizing = "Authorizing"
    Pending = "Pending"
    In_Process = "In Process"
    Complete = "Complete"
  

class TaskStatus(object):
    COMPLETE = "COMPLETE"
    INPROGRESS = "INPROGRESS"
    ABORTED = "ABORTED"
    FAILED = "FAILED"
  

class Priority(object):
    ECONOMY = "ECONOMY"
    STANDARD = "STANDARD"
    PRIORITY = "PRIORITY"
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    all = "[ ECONOMY, STANDARD, PRIORITY, CRITICAL, HIGH ]"
  

class Fidelity(object):
    MECHANICAL = "MECHANICAL"
    HIGH = "HIGH"
    EXTERNAL = "EXTERNAL"
    PREMIUM = "PREMIUM"
    PROFESSIONAL = "PROFESSIONAL"
    all = "[ MECHANICAL, HIGH, EXTERNAL, PREMIUM, PROFESSIONAL ]"
  

class CaptionFormat(object):
    SRT = "SRT"
    SBV = "SBV"
    DFXP = "DFXP"
    QT = "QT"
    TRANSCRIPT = "TRANSCRIPT"
    TWX = "TWX"
    TPM = "TPM"
    WEB_VTT = "WEB_VTT"
    ECHO = "ECHO"
    all = "[ SRT, SBV, DFXP, QT, TRANSCRIPT, TWX, TPM, WEB_VTT, ECHO ]"


class TokenType(object):
    word = "word"
    punctuation = "punctuation"
    sound = "sound"
  

class Tag(object):
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
  

class SpeakerId(object):
    no = "no"
    number = "number"
    name = "name"
  

class SpeakerGender(object):
    UNKNOWN = "UNKNOWN"
    MALE = "MALE"
    FEMALE = "FEMALE"
  

class Case(object):
    upper = "upper"
    lower = "lower"
    unchanged = ""
  

class LineEnding(object):
    UNIX = "UNIX"
    WINDOWS = "WINDOWS"
    OSX = "OSX"


class CustomerApprovalSteps(object):
    TRANSLATION = "TRANSLATION"
    RETURN = "RETURN"
  

class CustomerApprovalTools(object):
    AMARA = "AMARA"
    CIELO24 = "CIELO24"
  

class Language(object):
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
    all = "[ en, fr, es, de, cmn, pt, jp, ar, ko, zh, hi, it, ru, tr, he ]"


class IWP(object):
    PREMIUM = "PREMIUM"
    INTERIM_PROFESSIONAL = "INTERIM_PROFESSIONAL"
    PROFESSIONAL = "PROFESSIONAL"
    SPEAKER_ID = "SPEAKER_ID"
    FINAL = "FINAL"
    MECHANICAL = "MECHANICAL"
    CUSTOMER_APPROVED_RETURN = "CUSTOMER_APPROVED_RETURN"
    CUSTOMER_APPROVED_TRANSLATION = "CUSTOMER_APPROVED_TRANSLATION"