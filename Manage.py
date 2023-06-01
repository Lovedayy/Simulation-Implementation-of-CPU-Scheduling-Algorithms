import threading
import time

import FileOperation
import Job_request_thread
import Process_scheduling_thread
import clock
import window


class Manage():
    def before_prepare(self):
        Job_request_thread.j.PCBqueue()
        Job_request_thread.j.PCB_list.sort(key=lambda x: x.InTimes)

    def get_output(self):
        # 将进程运行结果输出到文本框中
        Job_request_thread.j.Put_PCB_Data()
        window.ui.pushButton.setText("运行结束")
        window.ui.pushButton.setEnabled(True)
        window.ui.pushButton_2.setEnabled(False)
        FileOperation.change_result_name()  # 改变结果文件名

    def thread_start(self):
        # 读取作业请求，创建进程，将进程添加到就绪队列等操作
        thread1 = threading.Thread(target=Job_request_thread.j.run)  # 创建Job_request_thread线程
        # 按照一定的调度算法从就绪队列中选择进程进行调度，
        # 将其分配给 CPU 进行执行，更新进程状态和就绪队列等操作。
        thread2 = threading.Thread(target=Process_scheduling_thread.p.run)  # 创建Process_scheduling_thread线程
        thread1.start()
        thread2.start()
        time.sleep(clock.Clock.sleep_time / 2)  # 等待一会，使得初始化完成
        while (clock.Clock.pause == 0):  # 持续刷新页面直到两个线程运行结束
            window.ui.slotAdd()
        self.get_output()  # 获取结果


t = Manage()
