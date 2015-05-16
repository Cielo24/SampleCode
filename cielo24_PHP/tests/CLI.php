<?php

require_once "../vendor/autoload.php";
include "../src/cielo24/Actions.php";

$actions = new Actions("http://api-dev.cieo24.com");
$code = "\$actions->" . $argv[1];
$result = eval($code);
print((string)$result);

# Usage:
# >  php CLI.php 'login("username", "password");'
# ! Pay attention to quotation marks !