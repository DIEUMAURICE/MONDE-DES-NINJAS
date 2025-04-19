#!/bin/bash
gunicorn --bind 0.0.0.0:$PORT Narutogamebot_stats_persistent:app