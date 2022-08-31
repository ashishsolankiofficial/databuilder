# Will be used to format data from zomato dump

import pandas as pd
import os

master_restaurant = []

for f in range(1, 5):
    json_file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "data-source/file" + str(f) + ".json",
    )
    df = pd.read_json(json_file_path)

    for i in df["restaurants"]:
        if not isinstance(i, float):
            for j in i:
                restaurant_detail = j["restaurant"]
                restaurant_detail["R"] = restaurant_detail["R"]["res_id"]
                restaurant_detail["address"] = restaurant_detail["location"]["address"]
                restaurant_detail["locality"] = restaurant_detail["location"][
                    "locality"
                ]
                restaurant_detail["city"] = restaurant_detail["location"]["city"]
                restaurant_detail["city_id"] = restaurant_detail["location"]["city_id"]
                restaurant_detail["latitude"] = restaurant_detail["location"][
                    "latitude"
                ]
                restaurant_detail["longitude"] = restaurant_detail["location"][
                    "longitude"
                ]
                restaurant_detail["zipcode"] = restaurant_detail["location"]["zipcode"]
                restaurant_detail["country_id"] = restaurant_detail["location"][
                    "country_id"
                ]
                restaurant_detail["locality_verbose"] = restaurant_detail["location"][
                    "locality_verbose"
                ]
                restaurant_detail["zomato_events"] = {}
                restaurant_detail["order_url"] = {}
                restaurant_detail["order_deeplink"] = {}
                del restaurant_detail["apikey"]
                del restaurant_detail["location"]
                del restaurant_detail["user_rating"]
                del restaurant_detail["zomato_events"]
                del restaurant_detail["switch_to_order_menu"]
                del restaurant_detail["offers"]
                del restaurant_detail["establishment_types"]
                del restaurant_detail["order_url"]
                del restaurant_detail["order_deeplink"]
                del restaurant_detail["is_delivering_now"]
                del restaurant_detail["events_url"]
                del restaurant_detail["R"]
                master_restaurant.append(restaurant_detail)


df_master = pd.DataFrame(master_restaurant)
# df_master = df_master.iloc[:, 1:]
df_master.drop(df_master[df_master.country_id != 1].index, inplace=True)
df_master.drop_duplicates(subset=["name", "id"], keep=False, inplace=True)
df_master.to_csv("file1.csv", index=False)
