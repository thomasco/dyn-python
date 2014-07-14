import time

from dyn.traffic import DynTraffic

# create a new instance of the API client
dyn = DynTraffic('customername', 'username', 'password').with_zone('example.com')

# establish an API connection
dyn.session.create()

# create zone
dyn.zone.list()
dyn.zone.delete()
dyn.zone.create('admin2@example456.com', 60)

# create an A record
dyn.record.create('A', 'www.example456.com.', {'address':'1.2.3.4'})

# create cname record
dyn.record.create('CNAME', "something.example456.com", {'cname':'somethingelse.example456.com'})

# create http redirect
dyn.http_redirect.create('thisotherplace.example456.com','302','Y','http://thatplace.example456.com')

# allow time for updates to take place
time.sleep(10)

dyn.zone.publish()

# allow time for updates to take place
time.sleep(10)

# create gslb service
dyn.gslb.create('thisplace.example456.com', {'region_code':'global', 'pool':{'address':'anotherplace.example456.com'}}, {'protocol':'HTTPS', 'interval':'1'})

# publish changes
dyn.zone.publish()

# log out to finish session
dyn.session.destroy()


