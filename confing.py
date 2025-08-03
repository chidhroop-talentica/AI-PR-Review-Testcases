import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
TARGET_WEBSITE = os.getenv("TARGET_WEBSITE", "http://mission-codex.s3-website.ap-south-1.amazonaws.com/")
OPENAI_API_KEY = os.getenv("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")
BROWSER_HEADLESS = os.getenv("BROWSER_HEADLESS", "true").lower() == "true"
BROWSER_TIMEOUT = int(os.getenv("BROWSER_TIMEOUT", "30"))

# API endpoint for testing
API_ENDPOINT = "http://13.204.81.166:8080/api/v1/review"

# Test data for API testing
TEST_API_DATA = {
    "prUrl": "https://github.com/open-sauced/app/pull/4077"
}

# API Headers for the new endpoint
API_HEADERS = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'http://mission-codex.s3-website.ap-south-1.amazonaws.com',
    'Referer': 'http://mission-codex.s3-website.ap-south-1.amazonaws.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'X-API-KEY': 'test-api-key-123'
} 
