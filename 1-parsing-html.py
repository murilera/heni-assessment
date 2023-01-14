from bs4 import BeautifulSoup


def open_file():
    with open("./data/webpage.html", "r") as f:
        contents = f.read()

    soup = BeautifulSoup(contents, "lxml")
    return soup


def parse_title(html):
    title = html.find("h1", attrs={"id": "main_center_0_lblLotPrimaryTitle"})
    return title.text.strip() if title else None


def parse_painting_name(html):
    painting_name = html.find(
        "h2", attrs={"id": "main_center_0_lblLotSecondaryTitle"}
    )
    return painting_name.text.strip() if painting_name else None


def parse_gbp_price(html):
    gbp_price = html.find(
        "span", attrs={"id": "main_center_0_lblPriceRealizedPrimary"}
    )
    return gbp_price.text.strip() if gbp_price else None


def parse_usd_price(html):
    usd_price = html.find(
        "div", attrs={"id": "main_center_0_lblPriceRealizedSecondary"}
    )
    return usd_price.text.strip() if usd_price else None


def parse_gbp_estimate(html):
    gbp_estimate = html.find(
        "span", attrs={"id": "main_center_0_lblPriceEstimatedPrimary"}
    )
    return gbp_estimate.text.strip() if gbp_estimate else None


def parse_usd_estimate(html):
    usd_estimate = html.find(
        "span", attrs={"id": "main_center_0_lblPriceEstimatedSecondary"}
    )
    return usd_estimate.text.strip() if usd_estimate else None


def parse_image_url(html):
    image_url = html.find("div", attrs={"id": "main_center_0_ch_social_block"})
    return image_url["data-imagepath-lot"] if image_url else None


def parse_saledate(html):
    saledate = html.find("span", attrs={"id": "main_center_0_lblSaleDate"})
    return saledate.text.strip() if saledate else None


if __name__ == "__main__":
    content = open_file()
    output = {}
    output["title"] = parse_title(content)
    output["painting_name"] = parse_painting_name(content)
    output["gbp_price"] = parse_gbp_price(content)
    output["usd_price"] = parse_usd_price(content)
    output["gbp_estimate"] = parse_gbp_estimate(content)
    output["usd_estimate"] = parse_usd_estimate(content)
    output["image_url"] = parse_image_url(content)
    output["saledate"] = parse_saledate(content)
    print(output)
