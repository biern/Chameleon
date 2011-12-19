<?php

/**
 * Productstatus module
 */
class productstatus extends modules
{
    /**
     * Add product status
     * @param string $name Name (required)
     * @return integer $productstatusId
     */
    public function add($name)
    {
        $this->check('name', $name, 'required');
            
        $sql = 'INSERT INTO productstatus (name,addid) VALUES (:name, :addid)';
        
        $stmt = $this->db->prepare($sql);
        $stmt->setString('name', $name);
        $stmt->setInt('addid', $this->userId);
            
        return $stmt->executeInsertId();
    }
}