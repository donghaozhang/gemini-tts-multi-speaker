"""Helper to load sample dialogue text from JSON."""

import json
import os
from functools import lru_cache


_FILE = os.path.join(os.path.dirname(__file__), "sample_dialogues.json")


@lru_cache(maxsize=None)
def _load_dialogues():
    with open(_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_dialogue(section, key):
    """Return dialogue text or script from the JSON file."""
    data = _load_dialogues()
    return data[section][key]
