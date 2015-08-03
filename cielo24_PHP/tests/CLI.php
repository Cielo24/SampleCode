<?php

require_once "../vendor/autoload.php";
include "../src/cielo24/Actions.php";

$actions = new Actions("http://api-dev.cielo24.com");
$code = "return \$actions->" . $argv[1];
$result = eval($code);
print_r($result);

# Usage:
# >  php CLI.php 'login("username", "password");'
# ! Pay attention to quotation marks !