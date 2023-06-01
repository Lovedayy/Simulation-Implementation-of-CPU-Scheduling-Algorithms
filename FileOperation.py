import clock
import os
import ProcessList

file_num = 0

def get_data(input):  # 对读取的数据进行处理使之可识别
    for i in range(len(input)):
        if input[i] == "":
            input.pop(i)
            continue
        input[i] = [int(x) for x in input[i].split(',')]
    return input

# 进程ID 到达时间 运行时间 优先级
def read_jobs(job_num):  # 读取进程作业
    with open(job_num, "r") as f:
        jobs = get_data(f.read().splitlines())
    return jobs

def get_instruc_data(num):  # 读取指令
    file = f"../input{file_num}/{num}.txt"
    with open(file, "r") as f:
        instruc = get_data(f.read().splitlines())
    return instruc

# 作业ID 作业提交时间 作业包含进程数 优先级
def write_new_jobs(sid, t, num):  # 写入新的作业
    with open(f"../input{file_num}/jobs-input.txt", "a") as f:
        f.write(f"\n{sid},{t},{num}")
    with open(f"../input{file_num}/{sid}.txt", "a") as f:
        for i in range(num):
            f.write(f"{i + 1},0\n")

def write_result(result):  # 写入结果
    with open(f"../output{file_num}/ProcessResults.txt", "a") as f:
        f.write(f"{result}\n")

def change_result_name():  # 修改结果文件名，使之符合要求
    try:  # 检测是否存在同名文件，如果有，则覆盖
        # 时间片轮转法 time_slice_scheduling
        if ProcessList.idea == 1:
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-time_slice.txt")
        # 多级反馈队列法 multilevel_feedback
        elif ProcessList.idea == 2:
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-multilevel_feedback.txt")
        # 先来先服务 first_come_first_served
        elif ProcessList.idea == 3:
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-FCFS.txt")
        # 短作业优先 shortest_job_first
        elif ProcessList.idea == 4:
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-shortest_job.txt")
        # 最高响应比 highest_response_ratio_
        elif ProcessList.idea == 5:
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-highest_response.txt")

    except:
        if ProcessList.idea == 1:
            os.remove(f"../output{file_num}/ProcessResults-{clock.Clock.current}-time_slice.txt")
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-time_slice.txt")
        elif ProcessList.idea == 2:
            os.remove(f"../output{file_num}/ProcessResults-{clock.Clock.current}-multilevel.txt")
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-multilevel.txt")
        elif ProcessList.idea == 3:
            os.remove(f"../output{file_num}/ProcessResults-{clock.Clock.current}-FCFS.txt")
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-FCFS.txt")
        elif ProcessList.idea == 4:
            os.remove(f"../output{file_num}/ProcessResults-{clock.Clock.current}-shortest_job.txt")
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-shortest_job.txt")
        elif ProcessList.idea == 5:
            os.remove(f"../output{file_num}/ProcessResults-{clock.Clock.current}-highest_response.txt")
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-highest_response.txt")
