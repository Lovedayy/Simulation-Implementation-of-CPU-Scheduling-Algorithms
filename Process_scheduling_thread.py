import clock
import time
import ProcessList
import CPU
import window


class Process_scheduling_thread(clock.Clock):
    def __init__(self):
        super().__init__()

    def run(self):
        self.setpause(0)  # 开始运行
        if self.is_pause():  # 设置停止条件
            return
        while self.is_pause() == 0:
            if ProcessList.idea == 1:    # 时间片轮转法进程调度
                self.run_time_slice()
            elif ProcessList.idea == 2:  # 多级反馈队列法进程调度
                self.multilevel_feedback()
            elif ProcessList.idea == 3:  # 先来先服务
                self.FCFS()
            elif ProcessList.idea == 4:  # 短作业优先
                self.shortest_job_first()
            elif ProcessList.idea == 5:  # 最高响应比
                self.highest_response_ratio()

    def ClockInterrupt(self):  # 时钟中断
        time.sleep(clock.Clock.sleep_time)
        self.addtime()

    def run_time_slice(self):  # 优先级时间片轮转法进程调度
        ProcessList.pro.ready_processes.sort(key=lambda x: (x.Priority, x.InTimes))
        if len(ProcessList.pro.ready_processes) != 0:  # 如果就绪队列不为空
            if ProcessList.pro.running_processes == None:
                ProcessList.pro.add_running_process()  # 添加运行队列
                return
            else:
                current_process = ProcessList.pro.running_processes
                current_process.InstrucNum -= 1
                current_process.down_priority()  # 每执行完一个时间片，优先级降低

                if current_process.InstrucNum == 0:  # 如果当前进程已完成执行
                    current_process.EndTimes = clock.Clock.current
                    ProcessList.pro.running_processes = None
                    window.ui.printf(f"{clock.Clock.current}:{current_process.ProID}:[完成]")
                    return

                current_process.RunTimes += 1  # 如果当前进程未完成执行，则更新其运行时间
        self.ClockInterrupt()  # 时钟中断
        if clock.Clock.pause == 0:
            window.ui.printf(f"{clock.Clock.current}:[CPU空闲]")

    def multilevel_feedback(self):  # 多级反馈队列进程调度
        # 如果三个就绪队列不为空
        if len(ProcessList.pro.ready_processes) != 0 or len(ProcessList.pro.ready_processes2) != 0 or len(
                ProcessList.pro.ready_processes3) != 0:
            # 将进程加入到多级反馈队列中
            ProcessList.pro.feedback_queue()
            return

        self.ClockInterrupt()  # 时钟中断
        if clock.Clock.pause == 0:
            window.ui.printf(f"{clock.Clock.current}:[CPU空闲]")

    def FCFS(self):  # 先来先服务
        if ProcessList.pro.running_processes is None and len(ProcessList.pro.ready_processes) != 0:  # 如果运行队列为空，且就绪队列不为空
            ProcessList.pro.add_running_process_no_time_slice()  # 添加运行队列
        elif ProcessList.pro.running_processes is not None:  # 如果运行队列不为空
            current_process = ProcessList.pro.running_processes
            current_process.InstrucNum -= 1  # 执行当前进程的指令
            if current_process.InstrucNum == 0:  # 如果当前进程已完成执行
                current_process.EndTimes = clock.Clock.current
                ProcessList.pro.running_processes = None
                window.ui.printf(f"{clock.Clock.current}:{current_process.ProID}:[完成]")
            else:
                self.ClockInterrupt()  # 时钟中断
                if clock.Clock.pause == 0:
                    window.ui.printf(f"{clock.Clock.current}:{current_process.ProID}")
        else:  # 运行队列为空，就绪队列也为空
            self.ClockInterrupt()  # 时钟中断
            if clock.Clock.pause == 0:
                window.ui.printf(f"{clock.Clock.current}:[CPU空闲]")

    def shortest_job_first(self):  # 短作业优先
        # 将就绪队列按照进程执行时间从短到长排序
        ProcessList.pro.ready_processes.sort(key=lambda x: x.RunTimes)
        if ProcessList.pro.running_processes is None and len(ProcessList.pro.ready_processes) != 0:  # 如果运行队列为空，且就绪队列不为空
            ProcessList.pro.add_running_process_no_time_slice()  # 添加运行队列
        elif ProcessList.pro.running_processes is not None:  # 如果运行队列不为空
            current_process = ProcessList.pro.running_processes
            current_process.InstrucNum -= 1  # 执行当前进程的指令
            if current_process.InstrucNum == 0:  # 如果当前进程已完成执行
                current_process.EndTimes = clock.Clock.current
                ProcessList.pro.running_processes = None
                window.ui.printf(f"{clock.Clock.current}:{current_process.ProID}:[完成]")
            else:
                self.ClockInterrupt()  # 时钟中断
                if clock.Clock.pause == 0:
                    window.ui.printf(f"{clock.Clock.current}:{current_process.ProID}")
        else:  # 运行队列为空，就绪队列也为空
            self.ClockInterrupt()  # 时钟中断
            if clock.Clock.pause == 0:
                window.ui.printf(f"{clock.Clock.current}:[CPU空闲]")

    def highest_response_ratio(self):  # 最高响应比
        # 计算响应比
        for process in ProcessList.pro.ready_processes:
            #RunTimes初始化有问题哈哈，换一个意思一样的InstrucNum
            process.ResponseRatio = (process.WaitTimes + process.InstrucNum) / process.InstrucNum

        # 将就绪队列按照响应比从高到低排序
        ProcessList.pro.ready_processes.sort(key=lambda x: x.ResponseRatio, reverse=True)

        if ProcessList.pro.running_processes is None and len(ProcessList.pro.ready_processes) != 0:  # 如果运行队列为空，且就绪队列不为空
            ProcessList.pro.add_running_process_no_time_slice()  # 添加运行队列
        elif ProcessList.pro.running_processes is not None:  # 如果运行队列不为空
            current_process = ProcessList.pro.running_processes
            current_process.InstrucNum -= 1  # 执行当前进程的指令
            if current_process.InstrucNum == 0:  # 如果当前进程已完成执行
                current_process.EndTimes = clock.Clock.current
                ProcessList.pro.running_processes = None
                window.ui.printf(f"{clock.Clock.current}:{current_process.ProID}:[完成]")
            else:
                self.ClockInterrupt()  # 时钟中断
                if clock.Clock.pause == 0:
                    window.ui.printf(f"{clock.Clock.current}:{current_process.ProID}")

                 # 更新等待时间
                for p in ProcessList.pro.ready_processes:
                    if p != current_process:
                        p.WaitTimes += 1

        else:  # 运行队列为空，就绪队列也为空
            self.ClockInterrupt()  # 时钟中断
            if clock.Clock.pause == 0:
                window.ui.printf(f"{clock.Clock.current}:[CPU空闲]")


p = Process_scheduling_thread()
