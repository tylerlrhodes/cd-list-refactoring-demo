#!/bin/bash

cd /web-app
uwsgi --ini app.ini &
nginx -g "daemon off;"

