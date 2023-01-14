import requests
import json
import math
import pandas as pd
from bs4 import BeautifulSoup


def request(page=1):
    url = f"https://www.bearspace.co.uk/purchase?page={page}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    return soup


def parse_ul(html):
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


def parse_product(product_list, outputs=[]):
    for product in product_list:
        output = {}
        output[
            "url"
        ] = "https://www.bearspace.co.uk/product-page/" + product.get(
            "urlPart"
        )
        output["title"] = product.get("name")
        output["media"] = product.get("media", [{}])[0].get("mediaType")
        output["height_cm"] = product.get("media", [{}])[0].get("height")
        output["width_cm"] = product.get("media", [{}])[0].get("width")
        output["price"] = product.get("price")
        outputs.append(output)

    return outputs


if __name__ == "__main__":
    offset = 20

    html = request()
    json_data = parse_ul(html)
    products_metadata = get_products_metadata(json_data, offset)
    total_products = get_total_products(products_metadata)
    pages = get_total_pages(total_products, offset)

    html = request(pages)
    json_data = parse_ul(html)
    products_metadata = get_products_metadata(json_data, offset * pages)
    products_list = get_products_list(products_metadata)
    outputs = parse_product(products_list)

    df = pd.DataFrame(outputs)
    print(df)
