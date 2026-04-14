FROM python:3.11-slim-bookworm

# Install dependencies for Playwright
RUN apt-get update && apt-get install -y \
    libnss3 \
    libatk-bridge2.0-0 \
    libdrm2 \
    libxkbcommon0 \
    libgbm1 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt scrapy scrapy-playwright

RUN playwright install-deps chromium
RUN playwright install chromium

COPY playwright-quotes.py .

CMD ["scrapy", "runspider", "playwright-quotes.py", "-o", "/output/results_playwright.json"]