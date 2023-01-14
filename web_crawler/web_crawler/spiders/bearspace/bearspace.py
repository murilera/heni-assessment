import scrapy
from web_crawler.spiders.bearspace import parser


class BearSpace(scrapy.Spider):
    name = "bearspace"
    url = "https://www.bearspace.co.uk/purchase?page={page}"
    offset = 20

    def start_requests(self):
        self.log("Starting spider")
        url = self.url.format(page="1")
        yield scrapy.Request(url=url, callback=self._handle_first_request)

    def _handle_first_request(self, response):
        json_data = parser.parse_ul(response)
        products_metadata = parser.get_products_metadata(
            json_data, self.offset
        )
        total_products = parser.get_total_products(products_metadata)
        pages = parser.get_total_pages(total_products, self.offset)
        return self.second_request(pages)

    def second_request(self, pages):
        url = self.url.format(page=pages)
        yield scrapy.Request(
            url=url,
            callback=self._handle_second_request,
            cb_kwargs={"pages": pages},
        )

    def _handle_second_request(self, response, pages):
        json_data = parser.parse_ul(response)
        products_metadata = parser.get_products_metadata(
            json_data, self.offset * pages
        )
        products_list = parser.get_products_list(products_metadata)
        for output in parser.parse_product(products_list):
            yield output
