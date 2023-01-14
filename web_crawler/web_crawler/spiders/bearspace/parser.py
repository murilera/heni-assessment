import json
import math
from bs4 import BeautifulSoup


def parse_ul(response):
    html = BeautifulSoup(response.text, "lxml")
    obj = html.find("script", attrs={"id": "wix-warmup-data"})
    return json.loads(obj.text)


def get_products_metadata(data, size):
    return (
        data.get("appsWarmupData", {})
        .get("1380b703-ce81-ff05-f115-39571d94dfcd", {})
        .get(f"gallery_GBP_compId=TPASection_isucjep3_limit={size}", {})
        .get("catalog", {})
        .get("category", {})
        .get("productsWithMetaData", {})
    )


def get_products_list(metadata):
    return metadata.get("list")


def get_total_products(data):
    return data.get("totalCount", 1)


def get_total_pages(total, size):
    return math.ceil(total / size)


def parse_product(product_list):
    product_url = "https://www.bearspace.co.uk/product-page/"
    for product in product_list:
        output = {}
        output["title"] = product.get("name")
        output["price"] = product.get("price")
        output["height_cm"] = product.get("media", [{}])[0].get("height")
        output["width_cm"] = product.get("media", [{}])[0].get("width")
        output["media"] = product.get("media", [{}])[0].get("mediaType")
        output["url"] = product_url + product.get("urlPart")
        yield output
