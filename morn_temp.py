from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('5015d7ee90e69e164a28774f7cf6ebec')
mgr = owm.weather_manager()

reg = owm.city_id_registry()
locations = reg.locations_for('Saint Petersburg', country='RU')

spb = locations[0]
lat = spb.lat
lon = spb.lon

one_call = mgr.one_call(lat, lon)
daily_weather = one_call.forecast_daily

morn_temp = list()

for i in range(5):
    date = daily_weather[i].reference_time('iso')
    morn = daily_weather[i].temperature('celsius').get('morn')
    morn_temp.append(morn)

avg_morn_temp = sum(morn_temp)/len(morn_temp)
max_morn_temp = max(morn_temp)

print('Средняя утренняя температура на следующие 5 дней(включая сегодня): {:.2}'.format(avg_morn_temp), 'градусов цельсия')
print('Максимальная утренняя температура на следующие 5 дней(включая сегодня): {:.3}'.format(max_morn_temp), 'градусов цельсия')
