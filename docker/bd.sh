#!/bin/bash

alembic upgrade head

cd src

exec uvicorn main:app --reload --host 0.0.0.0