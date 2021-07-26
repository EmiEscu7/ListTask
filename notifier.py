import sys, csv
import time, datetime
import schedule
from win10toast import ToastNotifier



class Notifier():

    def __init__(self):
        self.notifier = ToastNotifier()

    def have_notify(self, task):
        pass

    def read_first_task(self, name):
        file = open(name, newline='')
        reader = csv.reader(file, delimiter=';')
        row1 = next(reader)
        file.close()
        if (row1 == ''):
            return None
        return row1

    def job(self):
        pass

    def change(self, task):
        pass

    def run(self):
        schedule.every(30).seconds.do(self.job)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def str2datetime(self, date, time):
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:])
        hour = int(time[0:2])
        minute = int(time[3:5])
        second = int(time[6:])
        return datetime.datetime(year, month, day, hour, minute, second)


class Notifier24(Notifier):

    def have_notify(self, task):
        date = self.str2datetime(task[-2], task[-1])
        """ compare the date of the task with the current date. 
        If left 24 hours, show the notification """
        return (date - datetime.datetime.now() < datetime.timedelta(hours=24))            

    def job(self):
        first = self.read_first_task("tasks.csv")
        if(self.have_notify(first) and first != None):
            self.notifier.show_toast("EN 24 HORAS", first[1], first[2], duration = 10)
            self.change(first)
    
    def change(self, task):
        tasks = []
        file = open('tasks.csv', 'r', newline='')
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            tasks.append(row)
        file.close()
        file = open("tasks.csv", 'w', newline='')
        writer = csv.writer(file, delimiter=';')
        for row in tasks:
            if(row != task):
                writer.writerow(row)
            else:
                f = open("tasks6.csv", 'r', newline='')
                a_reader = csv.reader(f, delimiter=';')
                a_tasks = []
                for a_row in a_reader:
                    a_tasks.append(a_row)
                f.close()
                f = open("tasks6.csv", 'w', newline='')
                wrtr = csv.writer(f, delimiter=';')
                for a_task in a_tasks:
                    wrtr.writerow(a_task)
                wrtr.writerow(row)
                f.close()
        file.close()
        
    
class Notifier6(Notifier):

    def have_notify(self, task):
        date = self.str2datetime(task[-2], task[-1])
        """ compare the date of the task with the current date. 
        If left 6 hours, show the notification """
        return (date - datetime.datetime.now() < datetime.timedelta(hours=6))            

    def job(self):
        first = self.read_first_task("tasks6.csv")
        if(self.have_notify(first) and first != None):
            self.notifier.show_toast("EN 6 HORAS", first[1], first[2], duration = 10)
            self.change(first)
    
    def change(self, task):
        tasks = []
        file = open('tasks6.csv', 'r', newline='')
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            tasks.append(row)
        file.close()
        file = open("tasks6.csv", 'w', newline='')
        writer = csv.writer(file, delimiter=';')
        for row in tasks:
            if(row != task):
                writer.writerow(row)
            else:
                f = open("tasks1.csv", 'r', newline='')
                a_reader = csv.reader(f, delimiter=';')
                a_tasks = []
                for a_row in a_reader:
                    a_tasks.append(a_row)
                f.close()
                f = open("tasks1.csv", 'w', newline='')
                wrtr = csv.writer(f, delimiter=';')
                for a_task in a_tasks:
                    wrtr.writerow(a_task)
                wrtr.writerow(row)
                f.close()
        file.close()


class Notifier1(Notifier):
    
    def have_notify(self, task):
        date = self.str2datetime(task[-2], task[-1])
        """ compare the date of the task with the current date. 
        If left 1 hour, show the notification """
        return (date - datetime.datetime.now() < datetime.timedelta(hours=1))            

    def job(self):
        first = self.read_first_task("tasks1.csv")
        if(self.have_notify(first) and first != None):
            self.notifier.show_toast("EN 1 HORA", first[1], first[2], duration = 10)
            self.change(first)
    
    def change(self, task):
        tasks = []
        file = open('tasks1.csv', 'r', newline='')
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            tasks.append(row)
        file.close()
        file = open("tasks1.csv", 'w', newline='')
        writer = csv.writer(file, delimiter=';')
        for row in tasks:
            if(row != task):
                writer.writerow(row)
            else:
                f = open("tasks0.csv", 'r', newline='')
                a_reader = csv.reader(f, delimiter=';')
                a_tasks = []
                for a_row in a_reader:
                    a_tasks.append(a_row)
                f.close()
                f = open("tasks0.csv", 'w', newline='')
                wrtr = csv.writer(f, delimiter=';')
                for a_task in a_tasks:
                    wrtr.writerow(a_task)
                wrtr.writerow(row)
                f.close()
        file.close()

class Notifier0(Notifier):
    
    def have_notify(self, task):
        date = self.str2datetime(task[-2], task[-1])
        """ compare the date of the task with the current date. 
        If left 0 hour, show the notification """
        return (date - datetime.datetime.now() < datetime.timedelta(hours=0))            

    def job(self):
        first = self.read_first_task("tasks0.csv")
        if(self.have_notify(first) and first != None):
            self.notifier.show_toast("EN 0 HORAS", first[1], first[2], duration = 10)
            self.change(first)
    
    def change(self, task):
        tasks = []
        file = open('tasks0.csv', 'r', newline='')
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            tasks.append(row)
        file.close()
        file = open("tasks0.csv", 'w', newline='')
        writer = csv.writer(file, delimiter=';')
        for row in tasks:
            if(row != task):
                writer.writerow(row)
            else:
                f = open("tasks_finished.csv", 'r', newline='')
                a_reader = csv.reader(f, delimiter=';')
                a_tasks = []
                for a_row in a_reader:
                    a_tasks.append(a_row)
                f.close()
                f = open("tasks_finished.csv", 'w', newline='')
                wrtr = csv.writer(f, delimiter=';')
                for a_task in a_tasks:
                    wrtr.writerow(a_task)
                wrtr.writerow(row)
                f.close()
        file.close()



if(sys.argv[1] == "24"):
    notifier = Notifier24()
    print("notifier 24 executing...")
elif(sys.argv[1] == "6"):
    notifier = Notifier6()
    print("notifier 6 executing...")
elif(sys.argv[1] == "1"):
    notifier = Notifier1()
    print("notifier 1 executing...")
elif(sys.argv[1] == "0"):
    notifier = Notifier0()
    print("notifier 0 executing...")
notifier.run()