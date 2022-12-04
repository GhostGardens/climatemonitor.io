# climatemonitor.io
Raspberry Pi (3/4) project for taking temperature/humidity readings &amp; sending them to Google Cloud


Pi Zero Wireless won't work as the Google Cloud libraries aren't compatible with that processor.

For use with ATIMOSOS 1PC Wired DHT22/AM2302 Digital Temperature and Humidity Sensor

Recommended to have a Twilio account in order to run goodmorning.py

-------------------------------------

Create a bigquery table:

sensordata

asof	DATETIME	NULLABLE			

hostname	STRING	NULLABLE			

temperature	FLOAT	NULLABLE			

humidity	FLOAT	NULLABLE	

-------------------------------------

1) Install RPi for headless

2) Set goodmorning.py to execute after boot to ID; while this isn't necessary it's a nice feature to have the pi send SMS when it boots and notifies you of its IP

3) Create a cron job to execute sensor.py every minute
