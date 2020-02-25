import MySQLdb

conn = MySQLdb.connect("Rajasekaran.mysql.pythonanywhere-services.com","Rajasekaran","dhivya1994","Rajasekaran$RestaurantDB")

c = conn.cursor()

c.execute("SELECT  Restaurants.hotelname, actualtiming.distance, actualtiming.time as ActualTime, group_concat(traffic.traficplace) as Places, group_concat(traffic.possiblity) as Individual_Probability, (sum(traffic.possiblity) / count(traffic.possiblity)) as Probability  FROM Restaurants  INNER JOIN actualtiming ON actualtiming.hotelid=Restaurants.id INNER JOIN probability ON actualtiming.hotelid=probability.hotelid INNER JOIN traffic  ON traffic.id=probability.trafficid  where  actualtiming.distance< 1000  group by Restaurants.hotelname, actualtiming.distance, actualtiming.time;")

rows = c.fetchall()

for eachRow in rows:
    print (eachRow)
