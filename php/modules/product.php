<?php

/**
 * Product module
 */
class product extends modules
{
    /**
     * Add product
     * @param string $name Name (required, languageUnique)
     * @param string $url Www seo ('/^[A-Za-z0-9-_\",\'\s]+$/')
	 * @param integer $stock
	 * @param integer $vatId
	 * @param float $buyPrice
	 * @param float $sellPrice
	 * @param float $weight
     * @return integer $productId
     */
    public function add($name, $url, $stock, $vatId, $buyPrice, $sellPrice, $weight)
    {
        $this->check('name', $name, 'required');
        $this->check('name', $name, 'languageUnique', array('table' => 'producttranslation', 'column' => 'name'));
        $this->check('url', $url, 'format', '/^[A-Za-z0-9-_\",\'\s]+$/');
        $this->check('stock', $stock, 'format', '/[0-9]{1,}/');
        $this->check('vatId', $vatId, 'required');
        $this->check('buyPrice', $buyPrice, 'required');
        $this->check('buyPrice', $buyPrice, 'format', '/[0-9]{1,}/');
        $this->check('sellPrice', $sellPrice, 'required');
        $this->check('sellPrice', $sellPrice, 'format', '/[0-9]{1,}/');
        $this->check('weight', $weight, 'required');
        $this->check('weight', $weight, 'format', '/[0-9]{1,}/');
        
        $buyPrice = $this->commaToDot($buyPrice);
        $sellPrice = $this->commaToDot($sellPrice);
        $weight = $this->commaToDot($weight);
        
        $sql = 'INSERT INTO product
        			(idproduct, stock, vatid, buyprice, sellprice, weight, addid)
        		VALUES
        			(NULL, :stock, :vatid, :buyprice, :sellprice, :weight, :addid)';
        
        $stmt = $this->db->prepare($sql);
		$stmt->setInt('stock', $stock);
		$stmt->setInt('vatid', $vatId);
		$stmt->setFloat('buyprice', $buyPrice);
		$stmt->setFloat('sellprice', $sellPrice);
		$stmt->setFloat('weight', $weight);
        $stmt->setInt('addid', $this->userId);
        
		$productId = $stmt->executeInsertId();
		
		$sql = 'INSERT INTO producttranslation
					(productid, name, seo, languageid)
				VALUES
					(:productid, :name, :url, :languageid)';
		
		$stmt = $this->db->prepare($sql);
		$stmt->setInt('productid', $productId);
		$stmt->setString('name', $name);
		$stmt->setString('url', $url);
		$stmt->setInt('languageid', $this->languageId);
		$stmt->execute();
		
		$sql = 'INSERT INTO productsearch
					(productid, languageid, name)
				VALUES
					(:productid, :languageid, :name)';
		
		$stmt = $this->db->prepare($sql);
		$stmt->setInt('productid', $productId);
		$stmt->setInt('languageid', $this->languageId);
		$stmt->setString('name', $name);
		
		$stmt->execute();
		
		return $productId;
    }
    
    /**
     * Edit product basic information
     * @param integer $productId
     * @param string $name Name (required, languageUnique)
     * @param string $url Www seo ('/^[A-Za-z0-9-_\",\'\s]+$/')
     * @param integer $enable
     * @param string $ean
     * @param string $DelivelerCode
     * @param integer $producerId
     */
    public function editBasicInformation($productId, $name, $url, $enable, $ean, $DelivelerCode, $producerId)
    {
        $this->check('name', $name, 'required');
        $this->check('name', $name, 'languageUnique', array('table' => 'producttranslation', 'column' => 'name'));
        $this->check('url', $url, 'format', '/^[A-Za-z0-9-_\",\'\s]+$/');
        
		$sql = 'UPDATE
					producttranslation
				SET
					name = :name, seo = :url
				WHERE
					productid = :productid AND languageid = :languageid';
		
	    $stmt = $this->db->prepare($sql);
		$stmt->setInt('productid', $productId);
		$stmt->setString('name', $name);
		$stmt->setString('url', $url);
		$stmt->setInt('languageid', $this->languageId);
		$stmt->execute();
		
        $sql = 'UPDATE
        			product
        		SET
        			enable = :enable, ean = :ean, delivelercode = :delivelercode, producerid = :producerid
        		WHERE
        			idproduct = :idproduct';
        
        $stmt = $this->db->prepare($sql);
		$stmt->setInt('enable', $enable);
		$stmt->setInt('producerid', $producerId);
		$stmt->setString('ean', $ean);
		$stmt->setString('delivelercode', $DelivelerCode);
		$stmt->setInt('idproduct', $productId);
		$stmt->execute();


    }
    
    /**
     * Edit product meta information
	 * @param integer $productId
     * @param string $keywordTitle Keyword title
     * @param string $keyword Keywords 
     * @param string $keywordDescription Keywords description
     */
    public function editMeta($productId, $keywordTitle, $keyword, $keywordDescription)
    {
        $sql = 'UPDATE
        			producttranslation
        		SET
        			keyword_title = :keyword_title, keyword = :keyword, keyword_description = :keyword_description
        		WHERE
        			productid = :productid';
        
        $stmt = $this->db->prepare($sql);
		$stmt->setInt('productid', $productId);
		$stmt->setString('keyword_title', $keywordTitle);
		$stmt->setString('keyword', $keyword);
		$stmt->setString('keyword_description', $keywordDescription);
		$stmt->execute();
    }
    
    /**
     * Edit stock info
	 * @param integer $productId
	 * @param integer $stock
	 * @param boolean $trackStock
	 * @param float $shippingCost
     */
    public function editStock($productId, $stock, $trackStock, $shippingCost)
    {
        $shippingCost = $this->commaToDot($shippingCost);
        
        $sql = 'UPDATE product SET stock = :stock, trackstock = :trackstock, shippingcost = :shippingcost WHERE	productid = :productid';
        
        $stmt = $this->db->prepare($sql);
		$stmt->setInt('productid', $productId);
		$stmt->setInt('stock', $stock);
		$stmt->setInt('trackstock', $trackStock);
		$stmt->setFloat('shippingcost', $shippingCost);
		$stmt->execute();
    }
    
    /**
     * Add product to category
	 * @param integer $productId
	 * @param integer $categoryId
	 * @return integer $productCategoryId
     */
    public function addToCategory($productId, $categoryId)
    {
        $sql = 'INSERT INTO productcategory (productid, categoryid, addid) VALUES (:productid, :categoryid, :addid)';
        
        $stmt = $this->db->prepare($sql);
		$stmt->setInt('productid', $productId);
		$stmt->setInt('categoryid', $categoryId);
		$stmt->setInt('addid', $this->userId);
		
		return $stmt->executeInsertId();
    }
    
    public function editPrice($productId)
    {
        
    }
    
    /**
     * Add deliverer to product
     * @param integer $productId
     * @param integer $delivererId
     * @return integer $productDelivererId
     */
    public function deliverer($productId, $delivererId)
    {
        $sql = 'INSERT INTO productdeliverer (productid, delivererid, addid) VALUES (:productid, :delivererid, :addid)';
        
        $stmt = $this->db->prepare($sql);
		$stmt->setInt('productid', $productId);
		$stmt->setInt('delivererid', $delivererId);
		$stmt->setInt('addid', $this->userId);
		
		return $stmt->executeInsertId();
    }
}