#!/usr/bin/env python3
"""
Domain Setup Validation Script
Tests if your custom domain is properly configured to proxy to Streamlit Cloud
"""

import requests
import socket
import dns.resolver
import sys
import json
from urllib.parse import urlparse

def test_dns_resolution(domain):
    """Test DNS resolution for the domain"""
    try:
        # Try to resolve the domain
        ip = socket.gethostbyname(domain)
        print(f"✅ DNS Resolution: {domain} -> {ip}")
        return True
    except socket.gaierror as e:
        print(f"❌ DNS Resolution Failed: {e}")
        return False

def test_http_connection(url):
    """Test HTTP connection to the URL"""
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        print(f"✅ HTTP Connection: Status {response.status_code}")
        print(f"   Final URL: {response.url}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ HTTP Connection Failed: {e}")
        return False

def test_streamlit_app(url):
    """Test if the URL serves a Streamlit app"""
    try:
        response = requests.get(url, timeout=10)
        if "streamlit" in response.text.lower():
            print("✅ Streamlit App Detected")
            return True
        else:
            print("⚠️  Streamlit App Not Detected in Response")
            return False
    except Exception as e:
        print(f"❌ Streamlit Test Failed: {e}")
        return False

def main():
    if len(sys.argv) != 3:
        print("Usage: python domain-test.py <your-domain.com> <streamlit-url>")
        print("Example: python domain-test.py myapp.com https://my-app.streamlit.app")
        sys.exit(1)

    custom_domain = sys.argv[1]
    streamlit_url = sys.argv[2]

    print("🔍 Domain Setup Validation")
    print("=" * 40)
    print(f"Custom Domain: {custom_domain}")
    print(f"Streamlit URL: {streamlit_url}")
    print()

    # Test DNS resolution
    dns_ok = test_dns_resolution(custom_domain)

    # Test HTTP connection
    http_ok = test_http_connection(f"https://{custom_domain}")

    # Test Streamlit app
    streamlit_ok = test_streamlit_app(f"https://{custom_domain}")

    print()
    print("=" * 40)
    if dns_ok and http_ok and streamlit_ok:
        print("🎉 Domain setup appears to be working correctly!")
        print("Your custom domain should be accessible.")
    else:
        print("⚠️  Some tests failed. Check your domain configuration.")
        print("\nCommon issues:")
        print("- DNS propagation may take 24-48 hours")
        print("- SSL certificate may not be issued yet")
        print("- Proxy configuration may be incorrect")

if __name__ == "__main__":
    main()
