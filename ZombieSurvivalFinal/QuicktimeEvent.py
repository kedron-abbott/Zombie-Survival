import datetime, time

stop = "go"
start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(seconds=difficulty)

while True:
    key = raw_input("type: ")
    if key == "yes":
        stop = "stop"

    if stop == "stop" and datetime.datetime.now() < end_time:
        print ('You made it!')
        break;
    elif stop == "stop" and datetime.datetime.now() > end_time:
        print("you took too long!")
        break; #how do you break out of this when time is up???
    else:
        print("wrong");
