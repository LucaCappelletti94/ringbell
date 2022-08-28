"""Automatic dispatching only on exceptions with no wait time."""
from ._auto_ringbell import auto_ringbell

auto_ringbell(minimum_execution_time=0, only_exceptions=True)