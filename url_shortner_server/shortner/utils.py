"""The utils module defines many utility functions that don't fit into other specific modules."""

from os import getenv
import re
from urllib.parse import urlparse
from typing import Tuple

from dotenv import load_dotenv


def is_possibly_malicious(long_url: str) -> Tuple[bool, str | None]:
    """
    This function checks if a given URL is possibly malicious
    or contains phishing scams.

    It returns a tuple of with a boolean indicating the URL is
    in fact malicious, and a possible AnalysisID from VirusCheck.
    """
    load_dotenv()
    malicious = False

    # 1. Check for HTTPS
    if not long_url.startswith("https://"):
        malicious = True

    # 2. Check for suspicious patterns
    if re.search(r"(login|verify|account|secure|bank)", long_url.lower()):
        malicious = True

    # 3. Check for IP address usage in the domain
    parsed_url = urlparse(long_url)
    if re.match(r"^\d+\.\d+\.\d+\.\d+$", parsed_url.netloc):
        malicious = True

    # 4. Do VirusCheck
    VT_AK = getenv("VIRUSTOTAL_API_KEY")
    virus_check_analysis_id = None

    # return (malicious, virus_check_analysis_id)
    return malicious
