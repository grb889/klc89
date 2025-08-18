#!/usr/bin/env python3
"""Query crt.sh for subdomains related to a given domain.

This script fetches certificate transparency entries from the free crt.sh
service and extracts unique subdomains for the target domain.
"""

import argparse
import asyncio
import json
import sys
import aiohttp
from typing import Set

async def fetch_crtsh_async(session: aiohttp.ClientSession, domain: str) -> list[dict]:
    """Asynchronously fetch records from crt.sh for the given domain."""
    query = f"%25{domain}"
    url = f"https://crt.sh/?q={query}&output=json"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        async with session.get(url, headers=headers, timeout=10) as response:
            if response.status == 200:
                data = await response.text()
                # crt.sh returns an empty list for no results, which is valid JSON.
                if data:
                    return json.loads(data)
                return []
            else:
                sys.stderr.write(f"Error: Received status code {response.status} for {domain}\n")
                return []
    except aiohttp.ClientError as exc:
        sys.stderr.write(f"Error fetching data for {domain}: {exc}\n")
        return []
    except asyncio.TimeoutError:
        sys.stderr.write(f"Request to crt.sh for {domain} timed out.\n")
        return []

def extract_subdomains(records: list[dict], domain: str) -> Set[str]:
    """Extract unique subdomains from crt.sh JSON records."""
    subdomains: Set[str] = set()
    for entry in records:
        name_value = entry.get("name_value", "")
        for item in name_value.splitlines():
            item = item.strip().lower()
            if item.endswith(f".{domain}") or item == domain:
                subdomains.add(item)
    return subdomains

async def main() -> int:
    parser = argparse.ArgumentParser(description="List subdomains via crt.sh")
    parser.add_argument("domain", help="Domain to search, e.g. example.com")
    parser.add_argument("-o", "--output", help="Write results to a file")
    args = parser.parse_args()

    async with aiohttp.ClientSession() as session:
        records = await fetch_crtsh_async(session, args.domain)

    subdomains = extract_subdomains(records, args.domain)
    sorted_subdomains = sorted(list(subdomains))

    if not sorted_subdomains:
        sys.stderr.write(f"No subdomains found for {args.domain}.\n")
        return 1
    
    for sub in sorted_subdomains:
        print(sub)

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as fh:
                fh.write("\n".join(sorted_subdomains))
        except OSError as exc:
            sys.stderr.write(f"Error writing file: {exc}\n")
            return 1

    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(asyncio.run(main()))
    except KeyboardInterrupt:
        sys.stderr.write("\nProcess interrupted by user.\n")
        raise SystemExit(1)