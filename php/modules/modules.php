<?php

require_once('db.php');

require_once('validator.php');

/**
 * Modules main class
 * All modules MUST extends IT
 */
class modules
{
    public $db;
    
    public $validator;
    
     /**
     * User id
     */
    public $userId = 1;
    
    public static $languageId = 1;
    
    public function __construct()
    {
        // Set up DB connection
        $this->db = new db();
        
        // And validator
        $this->valid = new validator($this->db);
    }
    
    public function check($name, $value, $type, $options = null)
    {
        if (!is_null($options))
        {
            $this->valid->$type($name, $value, $options);    
        }
        else 
        {
            $this->valid->$type($name, $value);
        }
    }
}