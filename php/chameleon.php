<?php
// Include modules base class
require_once './modules/modules.php';

/**
 * Main class for chameleon
 */
class chameleon
{
    /**
     * User id
     */
    public $userId = 1;
    
    public $languageId = 1;
    
    /**
     * Do magic :)
     */
    public function __call($name, $arguments)
    {
        // Get module name from $name
        $moduleName = '';
        $strlenName = strlen($name);
        
        for ($i=0; $i<$strlenName; ++$i)
        {
            // Check if that letter is a big
            if ($name[$i] >= 'A' && $name[$i] <= 'Z')
            {
                break;
            }
            else
            {
                $moduleName .= $name[$i];
            }
        }
        
        $moduleName = lcfirst($moduleName);
                
        // Check if module exist
        if (file_exists('./modules/'.$moduleName.'.php'))
        {            
            // Include file
            require_once('./modules/'.$moduleName.'.php');
        }
        else
        {
             throw new chameleonException('Module doesn\'t exist');   
        }

        // Other part is action
        $action = lcfirst(substr($name, strlen($moduleName)));
        
        // Make new instance
        $instance = new $moduleName();
        $instance->userId = $this->userId;
        $instance->languageId = $this->languageId;

        if(method_exists($instance, $action))
        {
            // If exist - run method
            //$instance->$action($arguments);
            return call_user_func_array(array($instance, $action), $arguments);
        }
        else 
        {
            throw new chameleonException('Action doesn\'t exist');
        }
    }
    
    public function setUserId($userId)
    {
        $this->userId = $userId;
    }
    
    public function setLanguageId($languageId)
    {
        $this->languageId = $languageId;
    }
    
}

/**
 * Exception class
 * 
 */

class chameleonException extends Exception
{
    
}