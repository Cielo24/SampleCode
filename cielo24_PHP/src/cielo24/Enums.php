<?php

class TaskType
{
    const JOB_CREATED = "JOB_CREATED";
    const JOB_DELETED = "JOB_DELETED";
    const JOB_ADD_MEDIA = "JOB_ADD_MEDIA";
    const JOB_ADD_TRANSCRIPT = "JOB_ADD_TRANSCRIPT";
    const JOB_PERFORM_TRANSCRIPTION = "JOB_PERFORM_TRANSCRIPTION";
    const JOB_PERFORM_PREMIUM_SYNC = "JOB_PERFORM_PREMIUM_SYNC";
    const JOB_UPDATE_ELEMENTLIST = "JOB_UPDATE_ELEMENTLIST";
    const JOB_GET_TRANSCRIPT = "JOB_GET_TRANSCRIPT";
    const JOB_GET_CAPTION = "JOB_GET_CAPTION";
    const JOB_GET_ELEMENTLIST = "JOB_GET_ELEMENTLIST ";
}

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
    const Authorizing = "Authorizing";
    const Pending = "Pending";
    const In_Process = "In Process";
    const Complete = "Complete";
}

class TaskStatus
{
    const COMPLETE = "COMPLETE";
    const INPROGRESS = "INPROGRESS";
    const ABORTED = "ABORTED";
    const FAILED = "FAILED";
}

class Priority
{
    const ECONOMY = "ECONOMY";
    const STANDARD = "STANDARD";
    const PRIORITY = "PRIORITY";
    const CRITICAL = "CRITICAL";
    const HIGH = "HIGH";
}

class Fidelity
{
    const MECHANICAL = "MECHANICAL";
    const HIGH = "HIGH";
    const EXTERNAL = "EXTERNAL";
    const PREMIUM = "PREMIUM";
    const PROFESSIONAL = "PROFESSIONAL";
}

class CaptionFormat
{
    const SRT = "SRT";
    const SBV = "SBV";
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

class CustomerApprovalSteps
{
    const TRANSLATION_STEP = "TRANSLATION";
    const RETURN_STEP = "RETURN";
}

class CustomerApprovalTools
{
    const AMARA = "AMARA";
    const CIELO24 = "CIELO24";
}

class Languages
{
    const en = "en";
    const fr = "fr";
    const es = "es";
    const de = "de";
    const cmn = "cmn";
    const pt = "pt";
    const jp = "jp";
    const ar = "ar";
    const ko = "ko";
    const zh = "zh";
    const hi = "hi";
    const it = "it";
    const ru = "ru";
    const tr = "tr";
    const he = "he";
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