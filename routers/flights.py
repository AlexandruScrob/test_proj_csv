import json
import pandas as pd

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models.flights import Flight


router = APIRouter()


class NoEntryException(Exception):
    pass


FILE_NAME: str = "test_file.csv"
OUTPUT_FILE_NAME: str = "test_file_2.csv"


def get_flight_entry(flight_id: str):
    df = pd.read_csv(FILE_NAME)

    new_df = df.loc[df["flight ID"] == flight_id]
    if new_df.empty:
        raise NoEntryException("ERROR: no entry found with that ID")

    update_index = new_df.index.values[0]

    return update_index, df, new_df


@router.get("/flight/{flight_id}")
async def get_flight_info(flight_id: str) -> JSONResponse:
    try:
        update_index, _, new_df = get_flight_entry(flight_id)
        return JSONResponse(content=new_df.to_dict("index")[update_index])

    except NoEntryException as e:
        return JSONResponse(content=str(e))


@router.post("/flight/{flight_id}")
async def write_flight_Info(flight_id: str, flight_data: Flight) -> JSONResponse:
    try:
        update_index, df, _ = get_flight_entry(flight_id)

    except NoEntryException as e:
        return JSONResponse(content=str(e))

    # update with values of first result
    df.loc[update_index, "Arrival"] = flight_data.arrival
    df.loc[update_index, "Departure"] = flight_data.departure
    df.loc[update_index, "success"] = flight_data.success

    df.to_csv(OUTPUT_FILE_NAME, index=False)

    return JSONResponse(content=df.iloc[[update_index]].to_dict("index")[update_index])
