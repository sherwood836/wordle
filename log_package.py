def find_package(log_list, machine, timestamp):
    package_set = set()
    timestamp = int(timestamp)

    for log in log_list:
        insert_time = int(log[2])
        if machine == log[0] \
            and insert_time <= timestamp \
                and timestamp < insert_time + 3:
            package_set.add(log[1])

    return package_set

class PackageFinder:
    def __init__(log_list):
        pass

    def find_package(self, machine, timestamp):
        pass



import unittest

class FloydTest(unittest.TestCase):
    def test_find_package(self):
        log_list = [["m1", "p1", "1"],
                    ["m1", "p2", "2"],
                    ["m2", "p3", "3"],
                    ["m2", "p4", "4"],
                    ["m1", "p5", "5"],
                    ]
        machine = "m1"
        timestamp = "4"

        print(f"one find package: {find_package(log_list, machine, timestamp)}")


if __name__ == "__main__":
    unittest.main()