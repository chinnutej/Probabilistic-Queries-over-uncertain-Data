from flask import Flask, render_template, request

import MySQLdb

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/", methods=['GET','POST'])
def HomeWork():

    conn = MySQLdb.connect("dvenkate.mysql.pythonanywhere-services.com","Dhivya","dhivya1994","dvenkate$RestaurantDB")

    cur = conn.cursor()

    cur.execute("SELECT  Restaurants.hotelname, actualtiming.distance, actualtiming.time as ActualTime, group_concat(traffic.traficplace) as Places, group_concat(traffic.possiblity) as Individual_Probability, ROUND(((sum(traffic.possiblity)  +  (( (select count(*) from traffic) - (  select count(t.id) from probability p INNER JOIN traffic t on p.trafficid = t.id  where p.hotelid = actualtiming.hotelid   group by p.hotelid ) ) * 100 ) ) / ((select count(*) from traffic) *100 )), 3)  as Probability  FROM Restaurants  INNER JOIN actualtiming ON actualtiming.hotelid=Restaurants.id INNER JOIN probability ON actualtiming.hotelid=probability.hotelid INNER JOIN traffic  ON traffic.id=probability.trafficid  group by Restaurants.hotelname, actualtiming.distance, actualtiming.time;")

    rows = cur.fetchall()

    cur.close()

    if request.method == 'GET':
        return render_template('display.html', data=rows)
    if request.method == 'POST':
        if request.form['action'] == 'Get TOP-K Row':
            cur = conn.cursor()

            cur.execute("SELECT  Restaurants.hotelname, actualtiming.distance, actualtiming.time as ActualTime, group_concat(traffic.traficplace) as Places, group_concat(traffic.possiblity) as Individual_Probability,ROUND(((sum(traffic.possiblity)  +  (( (select count(*) from traffic) - (  select count(t.id) from probability p INNER JOIN traffic t on p.trafficid = t.id  where p.hotelid = actualtiming.hotelid   group by p.hotelid ) ) * 100 ) )  / ((select count(*) from traffic) *100 )), 3)  as Probability FROM Restaurants  INNER JOIN actualtiming ON actualtiming.hotelid=Restaurants.id INNER JOIN probability ON actualtiming.hotelid=probability.hotelid INNER JOIN traffic  ON traffic.id=probability.trafficid where  actualtiming.distance <= "+ request.form['distance']+  "  group by Restaurants.hotelname, actualtiming.distance, actualtiming.time HAVING Probability >= "+ request.form['probs'] +" ORDER BY Probability DESC LIMIT 1;")

            rows = cur.fetchall()

            cur.close()

            return render_template('display.html', data=rows)
        else:
            cur = conn.cursor()

            cur.execute("SELECT  Restaurants.hotelname, actualtiming.distance, actualtiming.time as ActualTime, group_concat(traffic.traficplace) as Places, group_concat(traffic.possiblity) as Individual_Probability,ROUND(((sum(traffic.possiblity)  +  (( (select count(*) from traffic) - (  select count(t.id) from probability p INNER JOIN traffic t on p.trafficid = t.id  where p.hotelid = actualtiming.hotelid   group by p.hotelid ) ) * 100 ) )  / ((select count(*) from traffic) *100 )), 3)  as Probability FROM Restaurants  INNER JOIN actualtiming ON actualtiming.hotelid=Restaurants.id INNER JOIN probability ON actualtiming.hotelid=probability.hotelid INNER JOIN traffic  ON traffic.id=probability.trafficid where  actualtiming.distance <= "+ request.form['distance']+  "  group by Restaurants.hotelname, actualtiming.distance, actualtiming.time HAVING Probability >= "+ request.form['probs'] +";")

            rows = cur.fetchall()

            cur.close()

            return render_template('display.html', data=rows)