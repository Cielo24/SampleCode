module Cielo24
  class BaseEnum < BasicObject
    def self.all
      all_enums = []
      self.constants(false).each{ |const_name|
        all_enums.push(self.const_get(const_name))
      }
      return all_enums
    end
  end

  class ErrorType < BaseEnum
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
  end

  class JobStatus < BaseEnum
    AUTHORIZING = 'Authorizing'
    PENDING = 'Pending'
    IN_PROCESS = 'In Process'
    COMPLETE = 'Complete'
    MEDIA_FAILURE = 'Media Failure'
    REVIEWING = 'Reviewing'
  end

  class Priority < BaseEnum
    ECONOMY = 'ECONOMY'
    STANDARD = 'STANDARD'
    PRIORITY = 'PRIORITY'
    CRITICAL = 'CRITICAL'
  end

  class Fidelity < BaseEnum
    MECHANICAL = 'MECHANICAL'
    PREMIUM = 'PREMIUM'
    PROFESSIONAL = 'PROFESSIONAL'
  end

  class CaptionFormat < BaseEnum
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
  end

  class TokenType < BaseEnum
    WORD = 'word'
    PUNCTUATION = 'punctuation'
    SOUND = 'sound'
  end

  class SoundTag < BaseEnum
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
  end

  class SpeakerId < BaseEnum
    NO = 'no'
    NUMBER = 'number'
    NAME = 'name'
  end

  class SpeakerGender < BaseEnum
    UNKNOWN = 'UNKNOWN'
    MALE = 'MALE'
    FEMALE = 'FEMALE'
  end

  class Case < BaseEnum
    UPPER = 'upper'
    LOWER = 'lower'
    UNCHANGED = ''
  end

  class LineEnding < BaseEnum
    UNIX = 'UNIX'
    WINDOWS = 'WINDOWS'
    OSX = 'OSX'
  end

  class CustomerApprovalStep < BaseEnum
    TRANSLATION = 'TRANSLATION'
    RETURN = 'RETURN'
  end

  class CustomerApprovalTool < BaseEnum
    AMARA = 'AMARA'
    CIELO24 = 'CIELO24'
  end

  class Language < BaseEnum
    ENGLISH = 'en'
    FRENCH = 'fr'
    SPANISH = 'es'
    GERMAN = 'de'
    MANDARIN_CHINESE = 'cmn'
    PORTUGUESE = 'pt'
    JAPANESE = 'jp'
    ARABIC = 'ar'
    KOREAN = 'ko'
    TRADITIONAL_CHINESE = 'zh'
    HINDI = 'hi'
    ITALIAN = 'it'
    RUSSIAN = 'ru'
    TURKISH = 'tr'
    HEBREW = 'he'
  end

  class IWP < BaseEnum
    PREMIUM = 'PREMIUM'
    INTERIM_PROFESSIONAL = 'INTERIM_PROFESSIONAL'
    PROFESSIONAL = 'PROFESSIONAL'
    SPEAKER_ID = 'SPEAKER_ID'
    FINAL = 'FINAL'
    MECHANICAL = 'MECHANICAL'
    CUSTOMER_APPROVED_RETURN = 'CUSTOMER_APPROVED_RETURN'
    CUSTOMER_APPROVED_TRANSLATION = 'CUSTOMER_APPROVED_TRANSLATION'
  end

  class JobDifficulty < BaseEnum
    GOOD = 'Good'
    BAD = 'Bad'
    UNKNOWN = 'Unknown'
  end
end