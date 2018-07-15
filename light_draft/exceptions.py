# coding: utf-8
"""Exceptions related to the application."""
from __future__ import unicode_literals

class DraftError(Exception):
    """Base error class for all the errors raised by the application."""

class CacheMissError(DraftError):
    """Snapshot was not found."""
