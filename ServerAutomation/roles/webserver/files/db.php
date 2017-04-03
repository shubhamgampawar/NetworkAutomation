<?php

$connection = new PDO('mysql:host=192.168.122.70;dbname=demo', 'demo', 'demo');
$statement  = $connection->query('SELECT message FROM demo');

echo $statement->fetchColumn();

