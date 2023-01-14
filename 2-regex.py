import pandas as pd


def open_csv():
    df = pd.read_csv("./data/dim_df_correct.csv")
    df = df.astype(str)
    return df


def parse_height(df, pattern):
    return df.height.str.extract(pattern).astype("float64")


def parse_width(df, pattern):
    return df.width.str.extract(pattern).astype("float64")


def parse_depth(df, pattern):
    return df.depth.str.extract(pattern).astype("float64")


if __name__ == "__main__":
    df = open_csv()
    pattern = r"(\d+.\d+)"
    height = parse_height(df, pattern)
    width = parse_width(df, pattern)
    depth = parse_depth(df, pattern)

    print(height)
    print(width)
    print(depth)
