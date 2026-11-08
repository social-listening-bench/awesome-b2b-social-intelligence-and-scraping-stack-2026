#!/usr/bin/env python3
"""
B2B Social Intelligence & Web Scraping Stack TCO Calculator 2026.
Combines Brand24 (Listening) + ScraperAPI (Web Extraction) + Webshare (Proxy Pool).
"""
import argparse

def calculate(data_volume_k, scraper_api_calls_k, proxy_count):
    # Brand24 Team ($149/mo annual)
    b24_cost = 149.0

    # ScraperAPI: Hobby $49/mo (100k calls) or Startup $149/mo (1M calls)
    scraper_cost = 49.0 if scraper_api_calls_k <= 100 else 149.0

    # Webshare: 100 proxies ~$18/mo or 250 proxies ~$40/mo
    proxy_cost = 18.0 if proxy_count <= 100 else (proxy_count * 0.16)

    total = b24_cost + scraper_cost + proxy_cost

    print("=" * 65)
    print("B2B Market Intelligence & Scraping Stack Budget 2026")
    print("=" * 65)
    print(f"1. Turnkey Social Listening (Brand24):   ${b24_cost:.2f}/mo")
    print(f"2. Custom Scraper API (ScraperAPI):      ${scraper_cost:.2f}/mo ({scraper_api_calls_k:,}k calls)")
    print(f"3. High-Concurrency Proxy (Webshare):    ${proxy_cost:.2f}/mo ({proxy_count} proxies)")
    print("-" * 65)
    print(f"Total Integrated Monthly Intelligence:   ${total:.2f}/mo")
    print("=" * 65)
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="B2B Intelligence Stack Calculator")
    parser.add_argument("--data-volume-k", type=int, default=5)
    parser.add_argument("--scraper-api-calls-k", type=int, default=100)
    parser.add_argument("--proxy-count", type=int, default=100)
    args = parser.parse_args()
    calculate(args.data_volume_k, args.scraper_api_calls_k, args.proxy_count)
