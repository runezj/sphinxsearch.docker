#!/bin/sh
sed -i -e s/\$SQL_HOST/$SQL_HOST/ /usr/local/etc/sphinx.conf
sed -i -e s/\$SQL_USER/$SQL_USER/ /usr/local/etc/sphinx.conf
sed -i -e s/\$SQL_PASS/$SQL_PASS/ /usr/local/etc/sphinx.conf
sed -i -e s/\$SQL_DB/$SQL_DB/ /usr/local/etc/sphinx.conf
