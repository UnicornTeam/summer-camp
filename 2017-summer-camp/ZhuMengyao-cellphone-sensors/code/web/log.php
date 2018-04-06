<?php
	$x = $_REQUEST['x'];
	$y = $_REQUEST['y'];
	$z = $_REQUEST['z'];
	$alpha = $_REQUEST['alpha'];
	$beta = $_REQUEST['beta'];
	$gamma = $_REQUEST['gamma'];
	print_r($_REQUEST);
	$fp = fopen("d:/device.txt", "a");//
	fwrite($fp, "$x $y $z $alpha $beta $gamma"."\r\n");
	
	fclose($fp);
	echo "ok";
?>