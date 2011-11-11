<?php

/**
 * Class used to contact with database
 * and validate input
 */
class db
{
    public $dbh;
    
    public function __construct($dbname = 'gekosale', $user = 'gekosale', $password = 'root')
    {
    	/* Connect to an ODBC database using driver invocation */
        $dsn = 'mysql:dbname='.$dbname.';host=localhost';
        
        try {
            $this->dbh = new PDO($dsn, $user, $password, array(PDO::ATTR_PERSISTENT => true, PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8"));
        } catch (PDOException $e) {
            echo 'Connection failed: ' . $e->getMessage();
        }
        
        $this->dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    }
    
    public function prepare($sql)
    {
        return new dbStatement($this->dbh, $sql);
    }
}

/**
 * Class that prepare given sql statement
 */
class dbStatement
{
    public $pdoStatement;
    
    public $dbh;
    
    public function __construct($dbh, $sql)
    {
        $this->dbh = $dbh;
        $this->pdoStatement = $this->dbh->prepare($sql);
        
        return $this;
    }
    
    /**
     * Bind int
     */
    public function setInt($name, $value)
    {
        $this->pdoStatement->bindValue(':'.$name, (int) $value, PDO::PARAM_INT);
        
        return $this;
    }
    
    /**
     * Bind float
     * @todo check float
     */
    public function setFloat($name, $value)
    {
        $this->pdoStatement->bindValue(':'.$name, (int) $value, PDO::PARAM_STR);
        
        return $this;
    }
    
    /**
     * Bind string
     */
    public function setString($name, $value)
    {
        $this->pdoStatement->bindValue(':'.$name, $value, PDO::PARAM_STR);
        
        return $this;
    }
    
    /**
     * Execute current statement
     */
    public function execute()
    {
       $this->pdoStatement->execute();
    }
    
    public function executeArray()
    {
        $this->pdoStatement->execute();
        
        return $this->pdoStatement->fetch(PDO::FETCH_ASSOC);
    }
    
    public function executeArrayAll()
    {
        $this->pdoStatement->execute();
        
        return $this->pdoStatement->fetchAll(PDO::FETCH_ASSOC);
    }
    
    public function executeInsertId()
    {
        $this->pdoStatement->execute();
        
        return $this->dbh->lastInsertId();
    }
}