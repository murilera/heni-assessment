## joins:
## the way I always thing is remembering set theory from high school

## imagine you have two sets A and B
## inner join: a match with things that are both in A and B
## left join: could be a union with what is in A and it's also in B or what is in A and doens't match with B
## right join: samething as left join, but at's B perspective
##  full joins: could be a union with everything in A and everything in B, but could also be what's in A and B without what's in both


import pandas as pd

flights = pd.read_csv("./data/flights.csv")
airports = pd.read_csv("./data/airports.csv")
weather = pd.read_csv("./data/weather.csv")
airlines = pd.read_csv("./data/airlines.csv")


def first_task():
    # SELECT f.arr_time, f.origin, f.dest, a.name FROM flights f LEFT JOIN airlines a ON f.carrier = a.carrier
    df = pd.merge(flights, airlines, on="carrier")
    result = df.filter(["arr_time", "origin", "dest", "name"], axis=1)
    print(result)
    return result


def second_task(df):
    # SELECT f.arr_time, f.origin, f.dest, a.name FROM flights f LEFT JOIN airlines a ON f.carrier = a.carrier WHERE a.name LIKE '%JetBlue%'
    result = df[df["name"].str.match("JetBlue") == True]
    print(result)
    return result


def third_task(df):
    # SELECT origin, coun"t(*) FROM result_df GROUP BY origin
    result = df.groupby(["origin"]).size().to_frame("size").reset_index()
    # result = df[["origin"]].value_counts().reset_index(name="count")
    print(result)
    return result


def fourth_task(df):
    # SELECT origin, count(*) FROM result_df GROUP BY origin HAVING COUNT(origin) > 100
    result = df[df["size"] > 100]
    print(result)
    return result


if __name__ == "__main__":
    d1 = first_task()
    d2 = second_task(d1)
    d3 = third_task(d2)
    d4 = fourth_task(d3)
