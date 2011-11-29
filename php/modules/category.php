<?php

/**
 * Category module
 */
class category extends modules
{
    /**
     * Add category
     * @param string $name Name (required)
     * @param string $www WWW
     * @param string $shortDescription = ''
     * @param string $description = ''
     * @param string $keywordTitle = '' Keyword title
     * @param string $keyword = '' Keywords 
     * @param string $keywordDescription = '' Keywords description
     * @param integer $distinction = 1
     * @param integer $enable = 1
     * @return integer $categoryId
     */
    public function add($categoryId, $name, $www, $shortDescription = '', $description = '',
                        $keywordTitle = '', $keyword = '', $keywordDescription = '', $distinction = 1, $enable = 1)
    {
        $this->check('name', $name, 'required');
            
        if ($categoryId == 0)
        {
            $sql = 'INSERT INTO category (categoryid, addid, distinction, enable) VALUES (NULL, :addid, :distinction, :enable)';
            
            $stmt = $this->db->prepare($sql);
            $stmt->setInt('addid', $this->userId);
    		$stmt->setInt('distinction', $distinction);
    		$stmt->setInt('enable', $enable);
            		    
            $categoryId = $stmt->executeInsertId();
        } else
        {
            $sql = 'UPDATE category SET distinction = :distinction, enable = :enable WHERE categoryid = :categoryid';
            $stmt = $this->db->prepare($sql);
            $stmt->setInt('distinction', $distinction);
    		$stmt->setInt('enable', $enable);
    		$stmt->execute();
        }
        
		$sql = 'INSERT INTO categorytranslation
					(categoryid,name,shortdescription, description, languageid, seo, keyword_title, keyword, keyword_description)
				VALUES
					(:categoryid,:name,:shortdescription, :description, :languageid, :seo, :keyword_title, :keyword, :keyword_description)';
		
		$stmt = $this->db->prepare($sql);
		$stmt->setInt('categoryid', $categoryId);
		$stmt->setString('name', $name);
		$stmt->setString('shortdescription', $shortDescription);
		$stmt->setString('description', $description);
		$stmt->setInt('languageid', $this->languageId);
		$stmt->setString('seo', $www);
		$stmt->setString('keyword_title', $keywordTitle);
		$stmt->setString('keyword', $keyword);
		$stmt->setString('keyword_description', $keywordDescription);
		$stmt->execute();
		
		return $categoryId;
    }
    
    /**
     * Change main category to given category
     * @param integer $categoryId
     * @param integer $mainCategoryId
     */
    public function changeMainCategory($categoryId, $mainCategoryId)
    {
        $sql = 'UPDATE category SET categoryid = :maincategoryid WHERE idcategory = :categoryid';
        
        $stmt = $this->db->prepare($sql);
		$stmt->setInt('categoryid', $categoryId);
        $stmt->setInt('maincategoryid', $mainCategoryId);
		$stmt->execute();
        
    }
}