import datetime
import pandas


def filter_by_date(
    df: pandas.core.frame.DataFrame, year: int, n: int
) -> pandas.core.frame.DataFrame:
    """
    Filter by date and the number of judgements in the mentioned timeframe

    Parameters:
            df: dataframe
            year: the year you are interested in
            n: the number of records
    """
    df["date_of_registration"] = pandas.to_datetime(df["dt_regis"])

    filtered_date_df = df[df["date_of_registration"].dt.year == year][:n]

    return filter_by_date_df
