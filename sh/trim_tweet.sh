#!/bin/bash 
sed -e 's/\(RT \)*@.\+[ :]//g' -e 's/\/*[http|t].*//g' -e 's/\\n//g' -e '/^$/d' $1
