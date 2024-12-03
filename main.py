import requests
from geopy.geocoders import Nominatim
import time
import smtplib

MY_EMAIL = "example@example.com"
MY_PASSWORD = "examplepassword"
MY_ANOTHER_MAIL = "example@example.com"
SUBJECT = "ISS Alert!"
iss_message = "Hey, look up! International Space Station is Passing in the sky."

tracker_on = True
while tracker_on:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data_dict = response.json()
    iss_latitude = iss_data_dict["iss_position"]["latitude"]
    iss_longitude = iss_data_dict["iss_position"]["longitude"]

    geolocater = Nominatim(user_agent="My_Locater")
    my_location = geolocater.geocode("Your adress")
    my_latitude = my_location.latitude
    my_longitude = my_location.longitude

    if (float(iss_latitude) - 5 <= my_latitude <= float(iss_latitude) + 5 and
        float(iss_longitude) - 5 <= my_longitude <= float(iss_longitude) + 5):
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            msg = f"Subject: {SUBJECT}\n\n{iss_message}"
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_ANOTHER_MAIL, msg=msg)
            tracker_on = False
    else:
        try:
            iss_location = geolocater.reverse(f"{iss_latitude}, {iss_longitude}")
            if iss_location:
                print(f"The International Space Station is over {iss_location}")
            else:
                print("International Space Station is currently over an area without a specific address.")
        except Exception as e:
            print(f"Couldn't determine ISS location: {e}")
        print(f"ISS coordinates: {iss_latitude}, {iss_longitude}")

    time.sleep(5.0)




