#!/usr/bin/env bash

source .env

uwsgi -s /tmp/dafi_webhooks.sock --manage-script-name --mount $ENDPOINT=app:app --uid www-data --gid www-data
