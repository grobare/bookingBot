import requests
from bs4 import BeautifulSoup


def search_hotels(destination, checkin_date, checkout_date, adults, rooms):
    url = f"https://www.booking.com/searchresults.en-gb.html?dest_id={destination}&dest_type=city&checkin_monthday={checkin_date}&checkin_year_month={checkin_date[0:4]}-{checkin_date[4:6]}&checkout_monthday={checkout_date}&checkout_year_month={checkout_date[0:4]}-{checkout_date[4:6]}&group_adults={adults}&no_rooms={rooms}"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    hotels = soup.find_all("div", class_="sr_property_block_main_row")
    for hotel in hotels:
        hotel_name = hotel.find("span", class_="sr-hotel__name").get_text(strip=True)
        hotel_score = hotel.find("div", class_="bui-review-score__badge").get_text(
            strip=True
        )
        hotel_price = hotel.find("div", class_="bui-price-display__value").get_text(
            strip=True
        )
        print(f"{hotel_name}: score {hotel_score}, price {hotel_price}")


search_hotels("3034", "20230515", "20230520", "2", "1")
