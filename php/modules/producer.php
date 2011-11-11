<?php

/**
 * Producer module
 */
class producer extends modules
{
    /**
     * Add producer or translation
     * @param integer $producerId If greater than 0, add only translation
     * @param string $name Name (required, languageUnique)
     * @param string $www Www address
     * @param string $email Email (required, email)
     * @param string $keywordTitle = '' Keyword title
     * @param string $keyword = '' Keywords 
     * @param string $keywordDescription = '' Keywords description
     * @param integer $photoId = 1
     * @return integer $producerId
     */
    public function add($producerId, $name, $www, $description, $keywordTitle = '', $keyword = '', $keywordDescription = '', $photoId = 1)
    {
        $this->check('name', $name, 'required');
        $this->check('name', $name, 'languageUnique', array('table' => 'producertranslation', 'column' => 'name'));
            
        if ($producerId == 0)
        {
            $sql = 'INSERT INTO producer (addid, photoid) VALUES (:addid, :photoid)';
            
            $stmt = $this->db->prepare($sql);
            $stmt->setInt('photoid', $photoId);
            $stmt->setInt('addid', $this->userId);
            
            $producerId = $stmt->executeInsertId();
        }
        
		$sql = 'INSERT INTO producertranslation (
			producerid,
			name, 
			seo, 
			description,
			keyword_title,
			keyword,
			keyword_description,
			languageid
		)
		VALUES 
		(
			:producerid,
			:name, 
			:seo,
			:description, 
			:keyword_title,
			:keyword,
			:keyword_description,
			:languageid
		)';
		
		$stmt = $this->db->prepare($sql);
		$stmt->setInt('producerid', $producerId);
		$stmt->setString('name', $name);
		$stmt->setString('seo', $www);
		$stmt->setString('description', $description);
		$stmt->setString('keyword_title', $keywordTitle);
		$stmt->setString('keyword', $keyword);
		$stmt->setString('keyword_description', $keywordDescription);
		$stmt->setInt('languageid', $this->languageId);
		$stmt->execute();	
        
		return $producerId;
    }
    
    /**
     * Add deliverer to producer
     * @param integer $delivererId
     * @param integer $producerId
     */
    public function addDeliverer($delivererId, $producerId)
    {    
        $sql = 'INSERT INTO producerdeliverer (delivererid, producerid, addid) VALUES (:delivererid, :producerid, :addid)';
		
        $stmt = $this->db->prepare($sql);
		$stmt->setInt('delivererid', $delivererId);
		$stmt->setInt('producerid', $producerId);
		$stmt->setInt('addid', $this->userId);
		$stmt->execute();
    }
}