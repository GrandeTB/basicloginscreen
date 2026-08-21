"""Utilities for an educational GUI access demo, not authentication."""


def normalise_display_name(value: str) -> str | None:
    """Return a display name for the demo, rejecting blank input."""
    name = value.strip()
    return name or None
