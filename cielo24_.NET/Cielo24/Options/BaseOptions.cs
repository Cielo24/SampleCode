using Cielo24.JSON;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;

namespace Cielo24.Options
{
    /* The base class. All of the other option classes inherit from it. */
    public abstract class BaseOptions
    {
        /* Returns a dictionary that contains key-value pairs of options, where key is the Name property
         * of the QueryName attribute assigned to every option and value is the value of the property.
         * Options with null value are not included in the dictionary. */
        public virtual Dictionary<string, string> GetDictionary()
        {
            Dictionary<string, string> queryDictionary = new Dictionary<string, string>();
            PropertyInfo[] properties = this.GetType().GetProperties();
            foreach (PropertyInfo property in properties)
            {
                object value = property.GetValue(this, null);
                if (value != null) // If property is null, don't include the key-value pair in the dictioanary
                {
                    QueryName key = (QueryName)property.GetCustomAttributes(typeof(QueryName), true).First();
                    queryDictionary.Add(key.Name, this.GetStringValue(value));
                }
            }
            return queryDictionary;
        }

        /* Returns a query string representation of options */
        public virtual string ToQuery()
        {
            Dictionary<string, string> queryDictionary = this.GetDictionary();
            return Utils.ToQuery(queryDictionary);
        }

        /* Sets the property whose QueryName attribute matches the key */
        public virtual void PopulateFromKeyValuePair(KeyValuePair<string, string> pair)
        {
            PropertyInfo[] properties = this.GetType().GetProperties();
            foreach (PropertyInfo property in properties)
            {
                QueryName key = (QueryName)property.GetCustomAttributes(typeof(QueryName), true).First();
                Type type = property.PropertyType;
                if (key.Name.Equals(pair.Key))
                {
                    property.SetValue(this, this.GetValueFromString(pair.Value, type), null);
                    return;
                }
            }
            throw new ArgumentException("Invalid Option: " + pair.Key);
        }

        // Array of strings in the key=value form 
        public void PopulateFromArray(string[] array)
        {
            foreach (string s in array ?? new string[0])
            {
                Dictionary<string, string> dictionary = Regex.Matches(s, "([^?=&]+)(=([^&]*))?").Cast<Match>().ToDictionary(x => x.Groups[1].Value, x => x.Groups[3].Value);
                this.PopulateFromKeyValuePair(dictionary.First());
            }
        }

        /* Converts string into an object */
        protected object GetValueFromString(string str, Type type)
        {
            object result = JsonConvert.DeserializeObject("\"" + str + "\"", type); // Quotes are necessary in json
            return result;
        }

        /* Converts 'value' into string based on its type. Precondition: value != null */
        protected string GetStringValue(object value)
        {
            if (value is List<string>)
            {
                return Utils.JoinQuoteList<string>((List<string>)value, ", ");
            }
            else if (value is List<Tag>)
            {
                return Utils.JoinQuoteList<Tag>((List<Tag>)value, ", ");
            }
            else if (value is List<Fidelity>)
            {
                return Utils.JoinQuoteList<Fidelity>((List<Fidelity>)value, ", ");
            }
            else if (value is char[])       // char[] (returned as (a, b))
            {
                return "(" + String.Join(", ", ((char[])value)) + ")";
            }
            else if (value is DateTime)     // DateTime (in ISO 8601 format)
            {
                return ((DateTime)value).ToString("yyyy-MM-ddTHH:mm:ss.fffffffzzz");
            }
            else                            // Takes care of the rest: int, bool, string, Uri
            {
                return value.ToString();
            }
        }
    }
}
