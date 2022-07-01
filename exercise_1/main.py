import pandas as pd
from datetime import datetime


def main():
   df = pd.read_csv("test.csv")
   sorted_flights = df.sort_values(by=["Arrival"])
   for index, row in sorted_flights.iterrows():
      time_delta_date = datetime.strptime(row.Departure.strip(), '%H:%M') - datetime.strptime(row.Arrival.strip(), '%H:%M')
      if time_delta_date.seconds > 10800:
         sorted_flights.loc[index, "success"] = "True"
      else:
         sorted_flights.loc[index, "success"] = "fail"

   sorted_flights.to_csv("test_2.csv", index=False)


if __name__ == "__main__":
   main()
