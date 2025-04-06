import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):

        # 1. Get the list of quotes availabe at the page
        quotes = response.css(".quote")
        for quote in quotes:

            # 2. Parse each quote found and yield the quote item
            yield {
                "quote": quote.css(".text::text").get(),
                "author": quote.css(".author::text").get(),
                "author_url": response.urljoin(
                    quote.css("span a::attr(href)").get()
                ),
                "tags": quote.css(".tag *::text").getall(),
            }

        # 3. Follow the next page link
        yield scrapy.Request(
            response.urljoin(response.css(".next a::attr(href)").get())
        )


# ---------------------  My solution  ----------------------


"""
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):

        # 1. Get the list of quotes availabe at the page
        for quote in response.css(".quote"):

            # 2. Parse each quote found and yield the quote item
            yield {
                "quote": quote.css("span.text::text").get(),
                "author": quote.css("small::text").get(),
                "url": response.urljoin(quote.css("span a::attr(href)").get()),
                "tags": quote.css(".tags a::text").getall(),
                # "urls_tag": response.urljoin(
                #     quote.css(".tags a::attr(href)").getall()
                # ),
            }

        # 3. Follow the next page link
        yield scrapy.Request(
            response.urljoin(response.css(".next a::attr(href)").get())
        )
        ...

"""
