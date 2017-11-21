import os


def refreshEP(IP, retry):
    reach = os.system('ping -c 3 ' + IP)
    print
    # validate IP and reachable
    # get Status(rest get)

    # Create EP with info(model and type NTP and dns info)

    # Compare Status(NTP/DNS) to config


#     if no match
#       rest update and refreshEP return EP
#     else
#       return EP

refreshEP("10.22.142.173", 1)
