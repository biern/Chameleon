<?php

/**
 * Deliverer module
 */
class deliverer extends modules
{
    /**
     * Add deliverer or translation
     * @param integer $delivererId If greater than 0, add only translation
     * @param string $name Name (required, languageUnique)
     * @param string $www Www address
     * @param string $email Email (required, email)
     * @param integer $photoId = 1
     * @return integer $delivererId
     */
    public function add($delivererId, $name, $www, $email, $photoId = 1)
    {
        $this->check('name', $name, 'required');
        $this->check('name', $name, 'languageUnique', array('table' => 'deliverertranslation', 'column' => 'name'));
        
        $this->check('email', $email, 'required');
        $this->check('email', $email, 'email');
    
        if ($delivererId == 0)
        {
            $sql = 'INSERT INTO deliverer (photoid, addid) VALUES (:photoid, :addid)';
            
            $stmt = $this->db->prepare($sql);
            $stmt->setInt('photoid', $photoId);
            $stmt->setInt('addid', $this->userId);
            
            $delivererId = $stmt->executeInsertId();
        }
        
		$sql = 'INSERT INTO deliverertranslation (delivererid, name, www, email, languageid)
				VALUES (:delivererid, :name, :www, :email, :languageid)';
		
		
		$stmt = $this->db->prepare($sql);
	    $stmt->setInt('delivererid', $delivererId);
		$stmt->setString('name', $name);
		$stmt->setString('www', $www);
		$stmt->setString('email', $email);
		$stmt->setInt('languageid', $this->languageId);
		$stmt->execute();	
        
		return $delivererId;
    }
}