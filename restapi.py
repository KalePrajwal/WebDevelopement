import pymysql as my
from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

class car(Resource):
    def get(self, mod):
        dic={}
        try:
            con = my.connect(host='bftwbvcwphfzfc96rmt8-mysql.services.clever-cloud.com', user='ubm6bcwfk0wgghj5', password='dkLqATSTs4TQ9ryVgopW', database='bftwbvcwphfzfc96rmt8')
            curs = con.cursor()
            curs.execute("select * from cars where model = '%s'" %mod)
            data = curs.fetchall()
            if data:
                dic['Model'] = data[0][0]
                dic['Company'] = data[0][1]
                dic['Type'] = data[0][2]
                dic['Engine'] = data[0][3]
                dic['Fuel'] = data[0][4]
                dic['Photo Link'] = data[0][5]
                dic['Price'] = data[0][6]
            else:
                dic['Result'] = 'Not Found'
            con.close()
        except:
            dic['Result'] = 'Error'
        return dic

class customer(Resource):
    def get(self, custid):
        dic={}
        try:
            con = my.connect(host='bftwbvcwphfzfc96rmt8-mysql.services.clever-cloud.com', user='ubm6bcwfk0wgghj5', password='dkLqATSTs4TQ9ryVgopW', database='bftwbvcwphfzfc96rmt8')
            curs = con.cursor()
            curs.execute("select * from customers where id = '%s'" %custid)
            data = curs.fetchall()
            if data:
                dic['Id'] = data[0][0]
                dic['Name'] = data[0][1]
                dic['Mobile'] = data[0][2]
                dic['Address'] = data[0][3]
            else:
                dic['Result'] = 'Not Found'
            con.close()
        except:
            dic['Result'] = 'error'
        return dic

api.add_resource(car, '/car/<mod>')
api.add_resource(customer, '/customer/<custid>')
app.run(debug=True)