<?php

/* The base class. All of the other option classes inherit from it. */

abstract class BaseOptions
{
    /* Returns a dictionary that contains key-value pairs of options, where key is the Name property
     * of the QueryName attribute assigned to every option and value is the value of the property.
     * Options with null value are not included in the dictionary. */
    public function getDictionary()
    {
        $dictionary = array();
        foreach ($this as $key => $value) {
            if ($value != null) { // If property is null, don't include the key-value pair in the dictionary
                if (is_bool($value)) {
                    $dictionary[$key] = ($value) ? "true" : "false";
                } else {
                    $dictionary[$key] = (string)$value;
                }
            }
        }
        return $dictionary;
    }

    public function toQuery()
    {
        $query_dict = $this->getDictionary();
        return http_build_query($query_dict);
    }
}