import pandas as pd
import numpy as np
def dataProcess(loader):
    features = []
    for i in loader:
        features.append(i)
    df = pd.DataFrame([features],
    columns=[   "book_title",
                "book_image_url",
                "book_desc",
                "book_genre",
                "book_authors",
                "book_format",
                "book_pages",
                "book_review_count",
                "book_rating_count"
                ])
    df["book_review_count"] = int(df["book_review_count"])
    df["book_rating_count"] = int(df["book_rating_count"])
    def process(x):
        return int(x.split(" ")[0])
    df["book_pages"] = df["book_pages"].apply(lambda x: process(x))
    formats_included = np.load("formats_included.npy").tolist()
    genres_included = np.load("genres_included.npy").tolist()
    for i in formats_included:
        df[i] = 0.
    df["other_format"] = 0.
    for i in genres_included:
        df[i] = 0.
    df["other_genre"] = 0.

    for i,value in enumerate(df["book_genre"]):
        temp  = value.split("|")
        for j in temp:
            if j not in genres_included:
                df.loc[i,["other_genre"]] = 1.
            else:
                df.loc[i,[j]] = 1.
    for i,j in enumerate(df["book_format"]):
        if j not in formats_included:
            df.loc[i,["other_format"]] = 1.
        else:
            df.loc[i,[j]] = 1.
    
    X = df.drop(['book_title', 'book_image_url', 'book_desc', 'book_genre', 'book_authors', 'book_format'], axis=1, inplace=False)
    return X
