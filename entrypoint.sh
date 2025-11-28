#!/bin/sh
set -e

python -m bot.recreate_database_postgres
exec python -u -m bot