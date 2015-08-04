<?php

class ErrorType
{
    const LOGIN_INVALID = "LOGIN_INVALID";
    const ACCOUNT_EXISTS = "ACCOUNT_EXISTS";
    const ACCOUNT_DOES_NOT_EXIST = "ACCOUNT_DOES_NOT_EXIST";
    const ACCOUNT_UNPRIVILEGED = "ACCOUNT_UNPRIVILEGED";
    const BAD_API_TOKEN = "BAD_API_TOKEN";
    const INVALID_QUERY = "INVALID_QUERY";
    const INVALID_OPTION = "INVALID_OPTION";
    const INVALID_URL = "INVALID_URL";
    const MISSING_PARAMETER = "MISSING_PARAMETER";
    const NOT_IMPLEMENTED = "NOT_IMPLEMENTED";
    const ITEM_NOT_FOUND = "ITEM_NOT_FOUND";
    const INVALID_RETURN_HANDLERS = "INVALID_RETURN_HANDLERS";
    const NOT_PARENT_ACCOUNT = "NOT_PARENT_ACCOUNT";
    const NO_CHILDREN_FOUND = "NO_CHILDREN_FOUND";
    const UNHANDLED_ERROR = "UNHANDLED_ERROR";
}

class JobStatus
{
    const AUTHORIZING = "Authorizing";
    const PENDING = "Pending";
    const IN_PROCESS = "In Process";
    const COMPLETE = "Complete";
    const MEDIA_FAILURE = 'Media Failure';
    const REVIEWING = 'Reviewing';
}

class Priority
{
    const ECONOMY = "ECONOMY";
    const STANDARD = "STANDARD";
    const PRIORITY = "PRIORITY";
    const CRITICAL = "CRITICAL";
}

class Fidelity
{
    const MECHANICAL = "MECHANICAL";
    const PREMIUM = "PREMIUM";
    const PROFESSIONAL = "PROFESSIONAL";
}

class CaptionFormat
{
    const SRT = "SRT";
    const SBV = "SBV";
    const SCC = "SCC";
    const DFXP = "DFXP";
    const QT = "QT";
    const TRANSCRIPT = "TRANSCRIPT";
    const TWX = "TWX";
    const TPM = "TPM";
    const WEB_VTT = "WEB_VTT";
    const ECHO_FORMAT = "ECHO";
}

class TokenType
{
    const WORD = "word";
    const PUNCTUATION = "punctuation";
    const SOUND = "sound";
}

class Tag
{
    const UNKNOWN = "UNKNOWN";
    const INAUDIBLE = "INAUDIBLE";
    const CROSSTALK = "CROSSTALK";
    const MUSIC = "MUSIC";
    const NOISE = "NOISE";
    const LAUGH = "LAUGH";
    const COUGH = "COUGH";
    const FOREIGN = "FOREIGN";
    const BLANK_AUDIO = "BLANK_AUDIO";
    const APPLAUSE = "APPLAUSE";
    const BLEEP = "BLEEP";
    const ENDS_SENTENCE = "ENDS_SENTENCE";
}

class SpeakerId
{
    const NO = "no";
    const NUMBER = "number";
    const NAME = "name";
}

class SpeakerGender
{
    const UNKNOWN = "UNKNOWN";
    const MALE = "MALE";
    const FEMALE = "FEMALE";
}

class TextCase
{
    const UPPER = "upper";
    const LOWER = "lower";
    const UNCHANGED = "";
}

class LineEnding
{
    const UNIX = "UNIX";
    const WINDOWS = "WINDOWS";
    const OSX = "OSX";
}

class CustomerApprovalStep
{
    const TRANSLATION_STEP = "TRANSLATION";
    const RETURN_STEP = "RETURN";
}

class CustomerApprovalTool
{
    const AMARA = "AMARA";
    const CIELO24 = "CIELO24";
}

class Language
{
    const ENGLISH = "en";
    const FRENCH = "fr";
    const SPANISH = "es";
    const GERMAN = "de";
    const MANDARIN_CHINESE = "cmn";
    const PORTUGUESE = "pt";
    const JAPANESE = "jp";
    const ARABIC = "ar";
    const KOREAN = "ko";
    const TRADITIONAL_CHINESE = "zh";
    const HINDI = "hi";
    const ITALIAN = "it";
    const RUSSIAN = "ru";
    const TURKISH = "tr";
    const HEBREW = "he";
}

class IWP
{
    const PREMIUM = "PREMIUM";
    const INTERIM_PROFESSIONAL = "INTERIM_PROFESSIONAL";
    const PROFESSIONAL = "PROFESSIONAL";
    const SPEAKER_ID = "SPEAKER_ID";
    const FINAL_ = "FINAL";
    const MECHANICAL = "MECHANICAL";
    const CUSTOMER_APPROVED_RETURN = "CUSTOMER_APPROVED_RETURN";
    const CUSTOMER_APPROVED_TRANSLATION = "CUSTOMER_APPROVED_TRANSLATION";
}

class JobDifficulty
{
    const GOOD = "Good";
    const BAD = "Bad";
    const UNKNOWN = "Unknown";
}