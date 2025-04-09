import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_complete"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        quotes = response.css(".quote")
        for quote in quotes:
            about_url = response.urljoin(quote.css("span a::attr(href)").get())

            quote_info = {
                "quote": quote.css(".text::text").get(),
                "author": quote.css(".author::text").get(),
                "author_url": about_url,
                "tags": quote.css(".tag *::text").getall(),
            }

            yield scrapy.Request(
                about_url,
                callback=self.parse_about_page,
                meta={"quote_info": quote_info},
                dont_filter=True,
            )

        yield scrapy.Request(
            response.urljoin(response.css(".next a::attr(href)").get()),
        )

    def parse_about_page(self, response):
        quote = response.meta["quote_info"]
        author_born_date = response.css(".author-born-date::text").get()
        quote["author_born_date"] = author_born_date
        yield quote


# ---------------------  My solution  ----------------------


"""


class QuotesSpider(scrapy.Spider):
    name = "quotes_complete"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        # This exercise is an improvement of Exercise 1
        # so you could use it as a start point
        quotes = response.css(".quote")
        for quote in quotes:
            author_url = response.urljoin(
                quote.css("span a::attr(href)").get()
            )
            incomplete_quote = {
                "quote": quote.css(".text::text").get(),
                "author": quote.css(".author::text").get(),
                "author_url": author_url,
                "tags": quote.css(".tag *::text").getall(),
            }

            # How to send the partially filled item to a new page?
            yield scrapy.Request(
                author_url,
                cb_kwargs={
                    "quote": incomplete_quote,
                },
                callback=self.parse_about_page,
                dont_filter=True,
            )

        yield scrapy.Request(
            response.urljoin(response.css(".next a::attr(href)").get())
        )

    def parse_about_page(self, response, quote):
        # We need to parse about page as well
        author_born_date = response.css(".author-born-date::text").get()
        quote["author_born_date"] = author_born_date
        yield quote


"""
