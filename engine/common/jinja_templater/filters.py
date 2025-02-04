import json

from django.utils.dateparse import parse_datetime


def datetimeformat(value, format="%H:%M / %d-%m-%Y"):
    try:
        return value.strftime(format)
    except AttributeError:
        return None


def iso8601_to_time(value):
    try:
        return parse_datetime(value)
    except (ValueError, AttributeError, TypeError):
        return None


def to_pretty_json(value):
    try:
        return json.dumps(value, sort_keys=True, indent=4, separators=(",", ": "), ensure_ascii=False)
    except (ValueError, AttributeError, TypeError):
        return None
