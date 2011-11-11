<?php

/**
 * WARNING!!
 * This is a test file, and it content may CHANGE!
 */

require_once('chameleon.php');

$api = new chameleon();

// Setup userId
$api->setUserId = 1;

$api->delivererAdd(0, 'Fabryka maszyn', 'http://www.fabryka.pl', 'dostawca@niepodam.pl');

