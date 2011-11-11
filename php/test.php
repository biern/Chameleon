<?php

/**
 * WARNING!!
 * This is a test file, and it content may CHANGE!
 */

require_once('chameleon.php');

$api = new chameleon();

// Setup userId
$api->setUserId = 1;

$delivererId = $api->delivererAdd(0, 'Fabryka maszyn', 'http://www.fabryka.pl', 'dostawca@niepodam.pl');

$producerId = $api->producerAdd(0, 'Producent szklanek', 'http://www.szklanki.pl', 'A to opis producenta',
				  'Keyword tytuł', 'Keywords słowa', 'Keyword opis');

$api->producerAddDeliverer($delivererId, $producerId);
