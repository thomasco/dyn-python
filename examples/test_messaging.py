import sys
from dyn.messaging import DynMessaging
import json

def show(message, result):
    sys.stderr.write(message + ": " + json.dumps(result) + '\n\n')

client = DynMessaging('your-api-key')
client._client.verbose = False

# accounts (create, list, list_xheaders, update, update_headers, destroy)
show("ACCOUNTS LIST", client.accounts.list())
show("ACCOUNTS CREATE", client.accounts.create("some@address.com", "secretword", "some company", "1234567890", "123 main st", "big city", "MA", "12345", "USA", "east", "bounces.com", "spam.com", "unsubscribe.com", "trackopens.com", "tracelinks.com", "trackunsubscribes.com", "generatenewapikey.com"))
show("ACCOUNTS UPDATE", client.accounts.update("some@address.com", "secretword", "some company", "1234567890", "123 main st", "big city", "MA", "12345", "USA", "east", "bounces.com", "spam.com", "unsubscribe.com", "trackopens.com", "tracelinks.com", "trackunsubscribes.com", "generatenewapikey.com"))
show("ACCOUNTS DESTROY", client.accounts.destroy("some@address.com"))
show("XHEADERS LIST", client.accounts.list_xheaders())
show("XHEADERS UPDATE", client.accounts.update_xheaders('X-MyExample1','X-AnotherExample2','X-Interesting3','X-Important4'))

# senders (list, details, status, create, update, dkim, destroy)
show("SENDERS LIST", client.senders.list())
show("SENDERS DETAILS", client.senders.details("some@address.com"))
show("SENDERS STATUS", client.senders.status("some@address.com"))
show("SENDERS CREATE", client.senders.create("some@address.com"))
show("SENDERS UPDATE", client.senders.update("some@address.com"))
show("SENDERS DKIM", client.senders.dkim("some@address.com", "123dkim"))
show("SENDERS DESTROY", client.senders.destroy("some@address.com"))

# recipients (status, activate)
show("RECIPIENTS STATUS", client.recipients.status("some@address.com"))
show("RECIPIENTS ACTIVATE", client.recipients.activate("some@address.com"))

# suppressions (list, count, create, activate)
show("SUPPRESSIONS LIST", client.suppressions.list())
show("SUPPRESSIONS COUNT", client.suppressions.count())
show("SUPPRESSIONS CREATE", client.suppressions.create("something@address.com"))
show("SUPPRESSIONS ACTIVATE", client.suppressions.activate("something@address.com"))

# send mail (send)
show("SEND MAIL", client.send_mail.send("something@address.com", "some@address.com", 'hello', 'from python api', "<html><body>'hi from python api'</body></html>", "somecopy@address.com", "something@address.com", "none"))

# report - delivery (list, count)
show("DELIVERY REPORT", client.delivery.list('2014-01-01','2014-08-01'))
show("DELIVERY COUNTS", client.delivery.count('2014-01-01','2014-08-01'))

# report - sent mail (list, count)
show("SENT MAIL REPORT", client.sent_mail.list('2014-01-01','2014-08-01'))
show("SENT MAIL COUNTS", client.sent_mail.count('2014-01-01','2014-08-01'))

# report - bounces (list, count)
show("BOUNCES REPORT", client.bounces.list('2014-01-01','2014-08-01'))
show("BOUNCES COUNTS", client.bounces.count('2014-01-01','2014-08-01'))

# report - complaints (list, count)
show("COMPLAINTS REPORT", client.complaints.list('2014-01-01','2014-08-01'))
show("COMPLAINTS COUNTS", client.complaints.count('2014-01-01','2014-08-01'))

# report - issues (list, count)
show("ISSUES REPORT", client.issues.list('2014-01-01','2014-08-01'))
show("ISSUES COUNTS", client.issues.count('2014-01-01','2014-08-01'))

# report - opens (list, count, unique, unique_count)
show("OPENS REPORT", client.opens.list('2014-01-01','2014-08-01'))
show("OPENS COUNTS", client.opens.count('2014-01-01','2014-08-01'))
show("OPENS REPORT UNIQUE", client.opens.unique('2014-01-01','2014-08-01'))
show("OPENS COUNTS UNIQUE", client.opens.unique_count('2014-01-01','2014-08-01'))

# clicks (list, count, unique, unique_count)
show("CLICKS REPORT", client.clicks.list('2014-01-01','2014-08-01'))
show("CLICKS COUNTS", client.clicks.count('2014-01-01','2014-08-01'))
show("CLICKS REPORT UNIQUE", client.clicks.unique('2014-01-01','2014-08-01'))
show("CLICKS COUNTS UNIQUE", client.clicks.unique_count('2014-01-01','2014-08-01'))
