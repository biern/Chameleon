<?php

/**
 * Validator based on FE_Rule* Validators from Gekosale
 * @see lib/FormEngine/Rules
 */
class validator
{
    public $db;
    
    public function __construct($db)
    {
        $this->db = $db;    
    }
	public function required($name, $value)
	{
		if (strlen($value) <= 0) {
		    throw new chameleonException($name.' is required'); 
		}
	}
	
	public function email($name, $value)
	{
	    if (preg_match('/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.(?:[A-Z]{2}|com|org|net|gov|mil|biz|info|mobi|name|aero|jobs|museum)$/i', $value) != 1)
	    {
	        throw new chameleonException($name.' must be valid email');     
	    }
	}
	
	public function format($name, $value, $options)
	{
	    if (preg_match($options, $value) != 1)
	    {
	        throw new chameleonException($name.' is not valid');      
	    }
	}
	
	public function languageUnique($name, $value, $options)
	{
	    $sql = "
			SELECT
				COUNT(*) AS items_count
			FROM
				".$options['table']."
			WHERE
				".$options['column']." = :value
				AND languageid = :language
		";
	    
		if ($options['exclude'] AND is_array($options['exclude'])) {
			if ( !is_array($this->_exclude['values']) ) {
				$options['values'] = Array($options['values']);
			}
			
			$excludedValues = implode(', ', $options['values']);
			
			$sql .= "AND NOT ".$options['column']." IN ({$excludedValues})";
		}
		
		$stmt = $this->db->prepare($sql);
		$stmt->setString('value', $value);
		$stmt->setString('language', modules::$languageId);
		
		$rs = $stmt->executeArray();
					
		if ($rs['items_count'] != 0)
		{
			throw new chameleonException($name.' must be language unique'); 
		}
	}
	
}

?>