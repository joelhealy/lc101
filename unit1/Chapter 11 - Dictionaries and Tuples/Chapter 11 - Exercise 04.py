#  Make a dictionary where the key is a worker’s name, and the value is a list
#  where the first element is the clock in time, second element is the clock
#  out time, and the third element is the total hours worked that day. Each
#  worker’s list starts at [0, 0, 0]. Create functions for clock_in and
#  clock_out.
#
#     clock_in takes the dictionary of workers, the name of the worker, and the
#     clock in time as parameters. When the worker clocks in, enter and save
#     their clock in time as the first element in the associated list value.
#
#     clock_out takes the same parameters, but with a clock out time instead
#     of clock in time. When the worker clocks out, enter and save their clock
#     out time and calculate the hours worked for that day and store it as the
#     third element in the list.
#
#  To make this program a little easier, we’re entering the clock in and
#  clock out times as integers. As a bonus mission, try adding the times as
#  strings representing the 24 hour clock (e.g., "08:00"), and then figure out
#  how to calculate the time worked. And you can do this exercise either by
#  aliasing or copying the dictionary.


def clock_in(dict, worker_name, clock_in_time):
    dict[worker_name] = [clock_in_time, 0, 0]


def clock_out(dict, worker_name, clock_out_time):
    dict[worker_name][1] = clock_out_time
    dict[worker_name][2] = clock_out_time - dict[worker_name][0]


def main():
    workers = {
        "George Spelvin": [0, 0, 0],
        "Jane Doe": [0, 0, 0],
        "John Smith": [0, 0, 0]}
    print(workers.get("George Spelvin"))   # should print [0,0,0]
    clock_in(workers, "George Spelvin", 8)
    clock_out(workers, "George Spelvin", 17)
    print(workers.get("George Spelvin"))   # should print [8, 17, 9]


if __name__ == "__main__":
    main()
