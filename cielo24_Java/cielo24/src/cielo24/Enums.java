package cielo24;

import com.google.gson.annotations.SerializedName;

public class Enums {

    public enum TaskType {
        JOB_CREATED,
        JOB_DELETED,
        JOB_ADD_MEDIA,
        JOB_ADD_TRANSCRIPT,
        JOB_PERFORM_TRANSCRIPTION,
        JOB_PERFORM_PREMIUM_SYNC,
        JOB_UPDATE_ELEMENTLIST,
        JOB_GET_TRANSCRIPT,
        JOB_GET_CAPTION,
        JOB_GET_ELEMENTLIST
    }

    public enum ErrorType {
        LOGIN_INVALID,
        ACCOUNT_EXISTS,
        ACCOUNT_DOES_NOT_EXIST,
        ACCOUNT_UNPRIVILEGED,
        BAD_API_TOKEN,
        INVALID_QUERY,
        INVALID_OPTION,
        INVALID_URL,
        MISSING_PARAMETER,
        NOT_IMPLEMENTED,
        ITEM_NOT_FOUND,
        INVALID_RETURN_HANDLERS,
        NOT_PARENT_ACCOUNT,
        NO_CHILDREN_FOUND,
        UNHANDLED_ERROR
    }

    public enum JobStatus {
        @SerializedName("Authorizing")
        AUTHORIZING,
        @SerializedName("Pending")
        PENDING,
        @SerializedName("In Process")
        IN_PROCESS,
        @SerializedName("Complete")
        COMPLETE,
        @SerializedName("Media Failure")
        MEDIA_FAILURE,
        @SerializedName("Reviewing")
        REVIEWING;

        @Override
        public String toString() {
            return Utils.getSerializedName(this);
        }
    }

    public enum TaskStatus {
        COMPLETE,
        INPROGRESS,
        ABORTED,
        FAILED
    }

    public enum Priority {
        ECONOMY,
        STANDARD,
        PRIORITY,
        CRITICAL
    }

    public enum Fidelity {
        MECHANICAL,
        PREMIUM,
        PROFESSIONAL
    }

    public enum CaptionFormat {
        SRT,
        SBV,
        SCC,
        DFXP,
        QT,
        TRANSCRIPT,
        TWX,
        TPM,
        WEB_VTT,
        ECHO
    }

    public enum TokenType {
        @SerializedName("word")
        WORD,
        @SerializedName("punctuation")
        PUNCTUATION,
        @SerializedName("sound")
        SOUND;

        @Override
        public String toString() {
            return Utils.getSerializedName(this);
        }
    }

    public enum Tag {
        UNKNOWN,
        INAUDIBLE,
        CROSSTALK,
        MUSIC,
        NOISE,
        LAUGH,
        COUGH,
        FOREIGN,
        BLANK_AUDIO,
        APPLAUSE,
        BLEEP,
        ENDS_SENTENCE
    }

    public enum SpeakerId {
        @SerializedName("no")
        NO,
        @SerializedName("number")
        NUMBER,
        @SerializedName("name")
        NAME;

        @Override
        public String toString() {
            return Utils.getSerializedName(this);
        }
    }

    public enum SpeakerGender {
        UNKNOWN,
        MALE,
        FEMALE
    }

    public enum Case {
        @SerializedName("upper")
        UPPER,
        @SerializedName("lower")
        LOWER,
        @SerializedName("")
        UNCHANGED;

        @Override
        public String toString() {
            return Utils.getSerializedName(this);
        }
    }

    public enum LineEnding {
        UNIX,
        WINDOWS,
        OSX
    }

    public enum CustomerApprovalStep {
        TRANSLATION,
        RETURN
    }

    public enum CustomerApprovalTool {
        AMARA,
        CIELO24
    }

    public enum Language {
        @SerializedName("en")
        ENGLISH,
        @SerializedName("fr")
        FRENCH,
        @SerializedName("es")
        SPANISH,
        @SerializedName("de")
        GERMAN,
        @SerializedName("cmn")
        MANDARIN_CHINESE,
        @SerializedName("pt")
        PORTUGUESE,
        @SerializedName("jp")
        JAPANESE,
        @SerializedName("ar")
        ARABIC,
        @SerializedName("ko")
        KOREAN,
        @SerializedName("zh")
        TRADITIONAL_CHINESE,
        @SerializedName("hi")
        HINDI,
        @SerializedName("it")
        ITALIAN,
        @SerializedName("ru")
        RUSSIAN,
        @SerializedName("tr")
        TURKISH,
        @SerializedName("he")
        HEBREW;

        @Override
        public String toString() {
            return Utils.getSerializedName(this);
        }
    }
    
    public enum IWP {
        PREMIUM,
        INTERIM_PROFESSIONAL,
        PROFESSIONAL,
        SPEAKER_ID,
        FINAL,
        MECHANICAL,
        CUSTOMER_APPROVED_RETURN,
        CUSTOMER_APPROVED_TRANSLATION
    }

    public enum JobDifficulty {
        @SerializedName("Good")
        GOOD,
        @SerializedName("Bad")
        BAD,
        @SerializedName("Unknown")
        UNKNOWN;

        @Override
        public String toString() {
            return Utils.getSerializedName(this);
        }
    }
}