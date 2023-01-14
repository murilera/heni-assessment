from datetime import datetime
from bs4 import BeautifulSoup


def open_file():
    with open("./data/webpage.html", "r") as f:
        contents = f.read()

    soup = BeautifulSoup(contents, "lxml")
    return soup


def parse_artist(html):
    artist = html.find("h1", attrs={"id": "main_center_0_lblLotPrimaryTitle"})
    return clear_artist_name(artist.text.strip()) if artist else None


def parse_painting_name(html):
    painting_name = html.find(
        "h2", attrs={"id": "main_center_0_lblLotSecondaryTitle"}
    )
    return painting_name.text.strip() if painting_name else None


def parse_gbp_price(html):
    gbp_price = html.find(
        "span", attrs={"id": "main_center_0_lblPriceRealizedPrimary"}
    )
    return clear_currency(gbp_price.text).strip() if gbp_price else None


def parse_usd_price(html):
    usd_price = html.find(
        "div", attrs={"id": "main_center_0_lblPriceRealizedSecondary"}
    )
    return clear_currency(usd_price.text).strip() if usd_price else None


def parse_gbp_estimate(html):
    gbp_estimate = html.find(
        "span", attrs={"id": "main_center_0_lblPriceEstimatedPrimary"}
    )

    return (
        format_estimates(clear_currency(gbp_estimate.text).strip().lstrip())
        if gbp_estimate
        else None
    )


def parse_usd_estimate(html):
    usd_estimate = html.find(
        "span", attrs={"id": "main_center_0_lblPriceEstimatedSecondary"}
    )
    return (
        format_estimates(clear_currency(usd_estimate.text).strip().lstrip())
        if usd_estimate
        else None
    )


def parse_image_url(html):
    image_url = html.find("div", attrs={"id": "main_center_0_ch_social_block"})
    return image_url["data-imagepath-lot"] if image_url else None


def parse_saledate(html):
    saledate = html.find("span", attrs={"id": "main_center_0_lblSaleDate"})
    return (
        format_date(saledate.text.strip().replace(",", ""))
        if saledate
        else None
    )


def clear_artist_name(value):
    return value.split("(")[0].strip()


def clear_currency(value):
    for c in ["GBP", "USD"]:
        value = value.replace(c, "")
    return value.replace(",", " ")


def format_estimates(value):
    value = value.replace("(", "").replace(")", "")
    return " , ".join(v.strip().lstrip() for v in value.split("-"))


def format_date(value):
    value = datetime.strptime(value, "%d %B %Y").strftime("%Y-%m-%d")
    return value


if __name__ == "__main__":
    content = open_file()
    output = {}
    output["artist"] = parse_artist(content)
    output["painting_name"] = parse_painting_name(content)
    output["gbp_price"] = parse_gbp_price(content)
    output["usd_price"] = parse_usd_price(content)
    output["gbp_estimate"] = parse_gbp_estimate(content)
    output["usd_estimate"] = parse_usd_estimate(content)
    output["image_url"] = parse_image_url(content)
    output["saledate"] = parse_saledate(content)
    print(output)
