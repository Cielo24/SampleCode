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
            if ($value != null) { // If property is null, don't include the key-value pair in the dictioanary
                $dictionary[$key] = $value;
            }
        }
        return $dictionary;
    }
}