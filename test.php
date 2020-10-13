<?php 

$command = escapeshellcmd('C:/Users/user/AppData/Local/Programs/Python/Python36/python.exe prediction.py');
$output = shell_exec($command);
echo $output;

?>