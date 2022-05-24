import pandas as pd


def get_random_rec(top_k):
    top_k = int(top_k)
    df = pd.read_csv("poster.csv", sep="\t")
    df.fillna("", inplace=True)
    return df.sample(top_k)


def get_model_rec(model, input_ids, top_k):
    ## implement your own model

    return get_random_rec(top_k)
