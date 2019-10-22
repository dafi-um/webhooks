#!/usr/bin/env bash

uwsgi --ini app.ini --uid www-data --gid www-data
