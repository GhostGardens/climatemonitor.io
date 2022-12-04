# climatemonitor.io
Raspberry Pi (3/4) project for taking temperature/humidity readings &amp; sending them to Google Cloud


Pi Zero Wireless won't work as the Google Cloud libraries aren't compatible with that processor.

For use with ATIMOSOS 1PC Wired DHT22/AM2302 Digital Temperature and Humidity Sensor

Create a bigquery table:
sensordata
asof	DATETIME	NULLABLE			
hostname	STRING	NULLABLE			
temperature	FLOAT	NULLABLE			
humidity	FLOAT	NULLABLE	

