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
        Authorizing, Pending, @SerializedName("In Process") In_Process, Complete
    }

    public enum TaskStatus {
        COMPLETE, INPROGRESS, ABORTED, FAILED
    }

    public enum Priority {
        ECONOMY, STANDARD, PRIORITY, CRITICAL, HIGH
    }

    public enum Fidelity {
        MECHANICAL, HIGH, EXTERNAL, PREMIUM, PROFESSIONAL
    }

    public enum CaptionFormat {
        SRT, SBV, DFXP, QT, TRANSCRIPT, TWX, TPM, WEB_VTT, ECHO
    }

    public enum TokenType {
        word, punctuation, sound
    }

    public enum Tag {
        UNKNOWN, INAUDIBLE, CROSSTALK, MUSIC, NOISE, LAUGH, COUGH, FOREIGN, BLANK_AUDIO, APPLAUSE, BLEEP, ENDS_SENTENCE
    }

    public enum SpeakerId {
        no, number, name
    }

    public enum SpeakerGender {
        UNKNOWN, MALE, FEMALE
    }

    public enum Case {
        upper, lower
    }

    public enum LineEnding {
        UNIX, WINDOWS, OSX
    }

    public enum CustomerApprovalSteps {
        TRANSLATION, RETURN
    }

    public enum CustomerApprovalTools {
        AMARA, CIELO24
    }

    public enum Languages {
        en, fr, es, de, cmn, pt, jp, ar, ko, zh, hi, it, ru, tr, he
    }
    
    public enum IWP {
        PREMIUM,
        INTERIM_PROFESSIONAL,
        PROFESSIONAL,
        SPEAKER_ID, FINAL,
        MECHANICAL,
        CUSTOMER_APPROVED_RETURN,
        CUSTOMER_APPROVED_TRANSLATION
    }
}