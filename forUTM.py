import utm

y = 479747.0453210057
x = 5377685.825323031
zone = 32
band = "U"
print(utm.to_latlon(y, x, zone, band))
print(utm.from_latlon(48.551944002183426, 8.725555999988195))
