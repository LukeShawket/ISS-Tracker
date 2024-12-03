# ISS-Tracker
# 🌌 Keep an Eye on the Stars with ISS Tracker 🌌     
Ever wondered when the International Space Station (ISS) is passing overhead? With ISS Tracker, you can stay updated and never miss a chance to spot the ISS in the night sky!    

# 🔍 Features:    

• Real-time Tracking: Get the latest coordinates of the ISS.

• Location Alerts: Receive an email alert when the ISS is near your location.

• Geolocation Magic: Uses geopy for accurate location identification.

• Space Station Updates: Know exactly where the ISS is, even over areas without specific addresses.

# 🛠️ Technologies Used:    

• Python: The core language of the project.

• Requests: For fetching the latest ISS data.

• Geopy: For geolocation services.

• SMTP: For sending email notifications.

• Open Notify API: Source of real-time ISS data.

# 🌠 How It Works:     

1. Fetch ISS Data: The script continuously fetches the latest coordinates of the ISS.

2. Geolocate Your Position: Uses geopy to find your exact location.

3. Compare Locations: Checks if the ISS is within a 5-degree range of your location.

4. Send Alerts: If the ISS is near, an email alert is sent to notify you.

5. Continuous Tracking: Keeps monitoring and providing updates until the ISS is nearby.

# 📧 Example Email Alert:    

Subject: ISS Alert!    
Hey, look up! The International Space Station is passing in the sky.    

# 🌟 Getting Started:

1. Clone the repository.

2. Install the required packages.

3. Update the email credentials in the script.
