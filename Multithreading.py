# MultiThreading = used to perform multile tasks at the same time 
# good for I/O bound tasks (networking, disk operations)

import threading
import time


def walk_dog():
    time.sleep(5)
    print("You finish walking the dog")

def take_out_trash():
    time.sleep(3)
    print("you take out the trash")

def get_mail():
    time.sleep(1)
    print("You get the mail")

chore1 = threading.Thread(target = walk_dog)
chore1.start()

chore2 = threading.Thread(target = take_out_trash)
chore2.start()

chore3 = threading.Thread(target = get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores completed!")