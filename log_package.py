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
    t_m_p_map = {}

    def __init__(self, log_list):

        for log in log_list:
            timestamp = int(log[2])

            if not self.t_m_p_map.get(timestamp):
                self.t_m_p_map[timestamp] = {}

            if not self.t_m_p_map.get(timestamp).get(log[0]):
                self.t_m_p_map[timestamp][log[0]] = set()

            self.t_m_p_map[timestamp][log[0]].add(log[1])


    def find_package(self, machine, timestamp):
        package_set = set()
        timestamp = int(timestamp)

        for each_time in range(timestamp - 2, timestamp):
            if self.t_m_p_map.get(each_time):
                if self.t_m_p_map.get(each_time).get(machine):
                    for package in self.t_m_p_map.get(each_time).get(machine):
                        package_set.add(package)

        return package_set

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
        self.assertEqual(set(['p2']), find_package(log_list, machine, timestamp))

        my_obj = PackageFinder(log_list)
        self.assertEqual(set(['p2']), my_obj.find_package(machine, timestamp))


if __name__ == "__main__":
    unittest.main()