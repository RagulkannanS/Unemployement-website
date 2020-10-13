<?php 

$command = escapeshellcmd('C:/Users/user/AppData/Local/Programs/Python/Python36/python.exe audio.py');
$output = shell_exec($command);
echo $output;


?>
<!DOCTYPE html>
<html>

<body>
<style>

{
	text-align:center; 
	background: url('speaker.gif') no-repeat center; 
	height: 150px;
}
</style>
</body>
</html>