from typing import List
from csv import reader
from config import CSV_PATH


def mean(values: List[float]) -> float:
    long = len(values)

    return sum(values) / long


def standard_deviation(mean: float):
    pass


def mean_distance(values: List[float], mean: float) -> List[float]:
    return list(map(lambda x: int(x - mean), values))


def main():

    individuo1 = {"cpx": [], "cpy": [], "mean": (0, 0)}
    individuo2 = {"cpx": [], "cpy": [], "mean": (0, 0)}

    with open(CSV_PATH) as csv_file:

        csv_reader = reader(csv_file, delimiter=",")

    next(csv_reader)
    next(csv_reader)

    for row in csv_reader:

        individuo1["cpx"].append(float(row[0]))
        individuo1["cpy"].append(float(row[1]))

        individuo2["cpx"].append(float(row[2]))
        individuo2["cpy"].append(float(row[3]))

    individuo1["mean"] = mean(individuo1["cpx"]), mean(individuo1["cpy"])
    individuo2["mean"] = mean(individuo2["cpx"]), mean(individuo2["cpy"])

    pass


if __name__ == "__main__":
    main()