import datetime
import threading
import csv

class Task():

    def __init__(self, name, description, date, time, priority):
        self.name = name
        self.description = description
        self.date = date
        self.time = time
        self.priority = priority


    def lt_date(self, date):
        return self.date < date
    
    def lt_time(self, time):
        return self.time < time
    
    def make_time(self, date, time):
        return datetime.datetime(int(date[6:]), int(date[3:5]), int(date[0:2]), int(time[0:2]), int(time[3:5]), int(time[6:]))

    def __lt__(self, task):
        my_time = self.make_time(self.date, self.time)
        other_time = self.make_time(task.getDate(), task.getTime())
        if(my_time < other_time):
            return True
        elif(my_time == other_time):
            if(self.priority < task.getPriority()):
                return True
            else:
                return False
        else:
            return False

    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getDate(self):
        return self.date
    
    def getPriority(self):
        return self.priority
    
    def getTime(self):
        return self.time
    
    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description
    
    def setDate(self, date):
        self.date = date

    def setPriority(self, priority): 
        self.priority = priority
    
    def setTime(self, time):
        self.time = time

    def __str__(self):
        return "name: " + self.name + "; description: " + self.description + "; date: " + self.date + "; time: " + self.time + "; priority: " + str(self.priority)
    
    def to_csv(self):
        return self.name + ";" + self.description + ";" + str(self.priority) + ";" + self.date + ";" + self.time
    
    

class Event(Task):

    def __init__(self, name, description, date, priority, hour):
        Task.__init__(self, name, description, date, time, priority)
        self.hour = hour
    
    def getHour():
        return self.hour
    
    def setHour(hour):
        self.hour = hour
    

class RepitTask(Task):

    def __init__(self, name, description, date, priority, interval, due_date):
        Task.__init__(self, name, description, date, time, priority)
        self.interval = interval
        self.due_date = due_date
    
    def getInterval():
        return self.interval
    
    def getDueDate():
        return self.due_date
    
    def setInterval(interval):
        self.interval = interval
    
    def setDueDate(due_date):
        self.due_date = due_date



class TaskManager():

    def __init__(self):
        self.type = {0: 'tasks.csv', 1: 'tasks6.csv', 2: 'tasks1.csv', 3: 'tasks0.csv', 4: 'tasks_finished.csv'}
        #self.upload_tasks()
    
    def upload_tasks(self, name):
        tasks = []
        file = open('tasks0.csv', newline='')
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            tasks.append(Task(row[0], row[1], row[3], row[4], row[2]))
        file.close()
        return tasks
        

    def addTask(self, task):
        type = self.in_what_file(task.getTime(), task.getDate())
        if(type == 0):
            self.save_file(self.tasks, self.type[type])
        elif(type == 1):
            self.save_file(self.tasks6, self.type[type])
        elif(type == 2):
            self.save_file(self.tasks1, self.type[type])
        else:
            self.save_file(self.tasks0, self.type[type])

    def in_what_file(self, time, date):
        date = self.str2date(date)
        now = str(datetime.datetime.now())
        difference = self.get_diff_hours(time, now)
        if(date > datetime.datetime.today()):
            return 0
        elif(difference > 360):
            return 1
        elif(difference > 60):
            return 2
        else:
            return 3

    """ get difference of hours between two times """
    def get_diff_hours(self, time1, now):
        year = int(now[0:4])
        month = int(now[5:7])
        day = int(now[8:10])
        time1 = datetime.datetime(year, month, day, int(time1[0:2]), int(time1[3:5]), int(time1[6:]))
        time2 = datetime.datetime(year, month, day, int(now[11:13]), int(now[14:16]), int(now[17:19]))
        return (time1 - time2).total_seconds() / 60

    def removeTask(self, task):
        pass
    
    def getTasks(self):
        return self.upload_tasks('tasks0.csv')

    def save_file(self, task, name):
        tasks = self.upload_tasks(name)
        tasks.append(task)
        tasks.sort()
        file = open(name, 'w')
        for task in tasks:
            file.write(task.to_csv())
            file.write('\n')
        file.close()
    
    def str2date(self, date):
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:])
        return datetime.datetime(year, month, day)
    
    """ str2time is a function that converts a string of the form HH:MM:SS to a datetime.time object"""
    def str2time(self, time):
        hour = int(time[0:2])
        minute = int(time[3:5])
        second = int(time[6:])
        return datetime.time(hour, minute, second)


"""
tarea1 = Task("Tarea", "Descripcion", "22/07/2021", "19:45:00", 2)
tarea2 = Task("Tarea2", "Descripcion2", "22/07/2021", "19:40:00", 2)

tManager = TaskManager()
tManager.addTask(tarea1)
tManager.addTask(tarea2)
"""
TaskManager()
print("task.py executing...")