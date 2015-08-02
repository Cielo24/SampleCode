using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text;

namespace Cielo24
{
    public enum TaskType
    {
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

    public enum ErrorType
    {
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

    [JsonConverter(typeof(DescriptionToEnumConverter))]
    public enum JobStatus
    {
        [Description("Authorizing")]
        AUTHORIZING,
        [Description("Pending")]
        PENDING,
        [Description("In Process")]
        IN_PROCESS,
        [Description("Complete")]
        COMPLETE,
        [Description("Reviewing")]
        REVIEWING,
        [Description("Media Failure")]
        MEDIA_FAILURE
    }

    public enum Priority
    {
        ECONOMY,
        STANDARD,
        PRIORITY,
        CRITICAL
    }

    [JsonConverter(typeof(FidelityToEnumConverter))]
    public enum Fidelity
    {
        MECHANICAL,
        PREMIUM,
        PROFESSIONAL
    }

    public enum CaptionFormat
    {
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

    [JsonConverter(typeof(DescriptionToEnumConverter))]
    public enum TokenType
    {
        [Description("word")]
        WORD,
        [Description("punctuation")]
        PUNCTUATION,
        [Description("sound")]
        SOUND
    }

    public enum Tag
    {
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
        GUESSED,
        ENDS_SENTENCE
    }

    [JsonConverter(typeof(DescriptionToEnumConverter))]
    public enum SpeakerId
    {
        [Description("no")]
        NO,
        [Description("number")]
        NUMBER,
        [Description("name")]
        NAME
    }

    public enum SpeakerGender
    {
        UNKNOWN,
        MALE,
        FEMALE
    }

    [JsonConverter(typeof(DescriptionToEnumConverter))]
    public enum Case {
        [Description("upper")]
        UPPER,
        [Description("lower")]
        LOWER,
        [Description("")]
        UNCHANGED
    }

    public enum LineEnding
    {
        UNIX,
        WINDOWS,
        OSX
    }

    public enum CustomerApprovalStep
    {
        TRANSLATION,
        RETURN
    }

    public enum CustomerApprovalTool
    {
        AMARA,
        CIELO24
    }

    [JsonConverter(typeof(DescriptionToEnumConverter))]
    public enum Language
    {
        [Description("en")]
        ENGLISH,
        [Description("fr")]
        FRENCH,
        [Description("es")]
        SPANISH,
        [Description("de")]
        GERMAN,
        [Description("cmn")]
        MANDARIN_CHINESE,
        [Description("pt")]
        PORTUGUESE,
        [Description("jp")]
        JAPANESE,
        [Description("ar")]
        ARABIC,
        [Description("ko")]
        KOREAN,
        [Description("zh")]
        TRADITIONAL_CHINESE,
        [Description("hi")]
        HINDI,
        [Description("it")]
        ITALIAN,
        [Description("ru")]
        RUSSIAN,
        [Description("tr")]
        TURKISH,
        [Description("he")]
        HEBREW
    }

    [JsonConverter(typeof(DescriptionToEnumConverter))]
    public enum JobDifficulty
    {
        [Description("Good")]
        GOOD,
        [Description("Bad")]
        BAD,
        [Description("Unknown")]
        UNKNOWN
    }

    /* Converts description into enum */
    public class DescriptionToEnumConverter : StringEnumConverter
    {
        public override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
        {
            // Nullable enums will cause a lot of trouble downstream if not converted to the underlying type
            if (Nullable.GetUnderlyingType(objectType) != null)
            {
                objectType = Nullable.GetUnderlyingType(objectType);
            }
            foreach (var val in objectType.GetEnumValues())
            {
                string name = Enum.GetName(objectType, val);
                FieldInfo field = objectType.GetField(name);
                DescriptionAttribute desc = Attribute.GetCustomAttribute(field, typeof(DescriptionAttribute)) as DescriptionAttribute;
                string description = desc.Description.ToLower();
                string readerValue = reader.Value.ToString().ToLower();
                if (description.Equals(readerValue))
                {
                    return val;
                }
            }
            // If could not convert
            return base.ReadJson(reader, objectType, existingValue, serializer);
        }
    }

    /* Converts Fidelity into enum (for mapping purposes) */
    public class FidelityToEnumConverter : StringEnumConverter
    {
        public override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
        {
            if (reader.Value == null)
            {
                return base.ReadJson(reader, objectType, existingValue, serializer);
            }
            else
            {
                string readerValue = reader.Value.ToString().ToUpper();
                if (readerValue.Equals("STANDARD"))
                {
                    return Fidelity.PREMIUM;
                }
                else if (readerValue.Equals("HIGH"))
                {
                    return Fidelity.PROFESSIONAL;
                }
                else
                {
                    return base.ReadJson(reader, objectType, existingValue, serializer);
                }
            }
        }
    }

    public static class EnumExtensionMethods
    {
        public static string GetDescription(this Enum value)
        {
            Type type = value.GetType();
            string name = Enum.GetName(type, value);
            if (name != null)
            {
                FieldInfo field = type.GetField(name);
                if (field != null)
                {
                    DescriptionAttribute desc = Attribute.GetCustomAttribute(field, typeof(DescriptionAttribute)) as DescriptionAttribute;
                    if (desc != null)
                    {
                        return desc.Description;
                    }
                }
            }
            return value.ToString();
        }
    }
}