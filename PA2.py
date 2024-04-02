
from Queue_for_ALGO import Queue
import random
from tabulate import tabulate

SECONDS_PER_ITEM = 4
OVERHEAD_SEC = 45

class Register:
    def __init__(self):
        self.current_cust = None
        self.checkout_time_remaining = 0
        
    def tick(self) :
        if not(self.idle()):
            self.checkout_time_remaining -= 1
            if self.checkout_time_remaining <= 0:
                self.current_cust = None
                
    def idle(self):
        return (self.current_cust == None)                
        
    def start_next(self, new_cust, cust_time):
        self.current_cust = new_cust
        self.checkout_time_remaining = cust_time
        
    def current_cust(self):
        return(self.current_cust)

class Customer:
    def __init__(self,time) :
        self.timestamp = time
        self.items = random.randint(6, 21)
        self.time = SECONDS_PER_ITEM * self.items + OVERHEAD_SEC
    
    def get_stamp(self) :
        return self.timestamp
        
    def get_items(self) :
        return self.items
    
    def get_time(self):
        return self.time
        
    def wait_time(self, current_time) :
        return current_time - self.timestamp
    
    def __repr__(self):
        return (str(self.items) + "|")
    
def add_cust(current_second, queues, total_lane_num):
    cust = Customer(current_second)
    index_list = [0]
    min_queue = int(1000000)
    for i in range(total_lane_num):
        if queues[i].size() < min_queue:
            index_list.pop()
            index_list.append(i)
            min_queue = queues[i].size()
        elif queues[i].size() == min_queue:
            index_list.append(i)
    if cust.get_items() >= 10 and 0 in index_list:
        index_list.remove(0)
    if 0 in index_list:
        chosen_register = 0
    elif len(index_list) == 1:
        chosen_register = index_list[0]   
    else:
        choice = random.randint(0, len(index_list) - 1)
        chosen_register = index_list[choice]
    queues[chosen_register].enqueue(cust)
    item_num = cust.get_items()
    return chosen_register, item_num
        

def simulation(sim_length, reg_lane_num):
    lanes = []
    queues = []
    waiting_times = []
    idle_times = []
    total_cust = []
    total_items = []
    total_lane_num = 1 + reg_lane_num
    
    #Creates Registers and Queues, as well as data storage lists
    for i in range(total_lane_num):   #+1 accounts for express lane
        lanes.append(Register())
        queues.append(Queue())
        waiting_times.append([])
        total_cust.append(0)
        total_items.append(0)
        idle_times.append(0)
    
    
    for current_second in range(sim_length):
        # adds a customer every 30 seconds
        if current_second % 30 == 0:
            chosen_register, item_num = add_cust(current_second, queues, total_lane_num)
            total_cust[chosen_register] += 1
            total_items[chosen_register] += item_num            
         
        #prints out which customers are in line every 50 seconds
        if current_second % 50 == 0:
            print("time = " + str(current_second))
            headers = ["reg #", "customers"]
            data = []
            for i in range(total_lane_num):
                temp = []
                temp.append(str(i) + ".")
                temp.append(queues[i].items)
                data.append(temp)
            table = tabulate(data,headers, tablefmt="grid")
            print(table)
            
        for i in range(total_lane_num):
            if lanes[i].idle():
                idle_times[i] += 1 / 60
                if (not queues[i].isEmpty()):
                    next_job = queues[i].dequeue()
                    lanes[i].start_next(next_job, next_job.get_time())
                    time_job_waited = next_job.wait_time(current_second)
                    waiting_times[i].append(time_job_waited)      
            lanes[i].tick()

    #Turns wait times into averages    
    average_list = []
    for i in range(total_lane_num):
        average_list.append(sum(waiting_times[i]) / (len(waiting_times[i]) + 1))
        
    #Formulates data for the final print statement
    headers2 = ["Reg", "Tot Cust", "tot items", "total idle time",
                "average wait time"]
    reg_list = ["express"]
    for i in range(reg_lane_num):
        reg_list.append(i)
    reg_list.append("total")
    total_cust.append(sum(total_cust))
    total_items.append(sum(total_items))
    average_list.append(sum(average_list)/5)
    idle_times.append(sum(idle_times))
        
    data2 = []
    for i in range(total_lane_num + 1): #+1 accounts for sum
        temp = []
        temp.append(reg_list[i])
        temp.append(total_cust[i])
        temp.append(total_items[i])
        temp.append(idle_times[i])
        temp.append(average_list[i])
        data2.append(temp)   
    table = tabulate(data2, headers2, tablefmt= "grid")
    print(table)   
        

def main():
    sim_runs = 12
    sim_seconds = 7200
    # Simulation loop for each second
    for i in range(sim_runs):
        print()
        for _ in range(sim_runs) :
            simulation(sim_seconds, 4) # num of regular lanes

main()
