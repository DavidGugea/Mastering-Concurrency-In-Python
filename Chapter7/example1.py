import multiprocessing


class ReductionConsumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        pname = self.name
        print("Using process {0}".format(pname))

        while True:
            num1 = self.task_queue.get()
            if num1 is None:
                print("Exiting process {0}".format(pname))
                self.task_queue.task_done()
                break

            self.task_queue.task_done()

            num2 = self.task_queue.get()
            if num2 is None:
                print("Reaching the end with process {0} and number {1}".format(pname, num1))
                self.task_queue.task_done()
                self.result_queue.put(num1)
                break

            print("Running process {0} on numbers {1} and {2}".format(pname, num1, num2))
            self.task_queue.task_done()
            self.result_queue.put(num1 + num2)
