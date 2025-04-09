import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_complete"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        # This exercise is an improvement of Exercise 1
        # so you could use it as a start point
        quotes = response.css(".quote")
        for quote in quotes:
            yield {
                "quote": quote.css(".text::text").get(),
                "author": quote.css(".author::text").get(),
                # The remaining data that we want requires that we gather data
                # from the content of this URL
                "author_url": response.urljoin(
                    quote.css("span a::attr(href)").get()
                ),
                "tags": quote.css(".tag *::text").getall(),
            }

            # How to send the partially filled item to a new page?

        yield scrapy.Request(
            response.urljoin(response.css(".next a::attr(href)").get())
        )

    def parse_about_page(self, response):
        # We need to parse about page as well
        ...
