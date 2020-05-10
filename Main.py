import serial

import time

XBEE = serial.Serial('COM4', 9600, timeout=None)

tot_power = 0

count = 0

seconds = time.time()

print('Start time', time.ctime(seconds))

while True:

    data = XBEE.readline() [:-2]

    count+=1

    if data:

        inst_watts = float(data.decode('utf-8'))

        inst_cost = inst_watts/1000*0.6

#        print('Ppower usage ', inst_watts, 'W; Costs ', inst_cost, 'p/hr')

        tot_power += inst_watts

    if count%3600 == 0:

        seconds = time.time()

#        print('Current time ', time.ctime(seconds), 'Hour power usage = ', tot_power/1000/3600, 'kWh')

        kWh = str(tot_power/3600/1000)

        seconds = time.time()

        time1 = str(time.ctime(seconds))

        s = (time1 + ';' + str(tot_power) + ';' + str(inst_watts) + ';' + kWh)

        s = s.replace(".", ",")

        print(s)

        with open("", "a") as data_file:

            data_file.write(s + "\n")

            data_file.close()

    elif count%60 == 0:

#        print ('Minute power usage = ', tot_power)

       

        seconds = time.time()

        time1 = str(time.ctime(seconds))

        s = (time1 + ';' + str(tot_power) + ';' + str(inst_watts))

        s = s.replace(".", ",")

        print(s)

        try:

            with open("", "a") as data_file:

                data_file.write(s + "\n")

                data_file.close()

        except IOError as err:

            errno, strerror = err.args

            print ("I/O error({0}): {1}".format(errno, strerror))

    

    time.sleep(1)
