from Module_12_1 import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        Vasya = Runner(self)
        for _ in range(10):
           return Runner.walk(Vasya)
        self.assertEqual(Runner.walk(Vasya),50)

    def test_run(self):
        Petya = Runner(self)
        for _ in range(10):
           return Runner.run(Petya)
        self.assertEqual(Runner.walk(Petya),100)

    def test_challenge(self):
        Ann = Runner(self)
        Kate = Runner(self)
        for _ in range(10):
           return Runner.run(Ann)
           return Runner.walk(Kate)
        self.assertNotEqual(Runner.walk(Ann),Runner.walk(Kate))

if __name__=="__main__":
    unittest.main()


