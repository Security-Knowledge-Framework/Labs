#!/usr/bin/env sh

./glauth32 -c sample-simple.cfg & 
python2 ldap-injection-harder.py