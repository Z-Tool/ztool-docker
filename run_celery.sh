#!/bin/bash
cd /jalpc
sleep 10
/usr/local/bin/celery worker -l info -A celery_worker.celery -B
