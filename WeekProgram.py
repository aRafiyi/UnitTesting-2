# Unit Testing
# Written on Feb 27 2020
# Testing for Valid Week day by day number

# Accompanying module: Week.py


import unittest 

def week(i):
    switcher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return switcher.get(i, "Invalid day of week")


class TestWeekMethod(unittest.TestCase):
    
    def test_Week_Day0_expectSunday(self):
        # Arrange
        i = 0
        expected = 'Sunday'
        
        # Act
        actual = week(i)
        
        # Assert
        self.assertEqual(expected, actual)
        
    def test_Week_Day1_expectMonday(self):
        # Arrange
        i = 1
        expected = 'Monday'
        
        # Act
        actual = week(i)
        
        # Assert
        self.assertEqual(expected, actual)
        
    def test_Week_Day2_expectTuesday(self):
        # Arrange
        i = 2
        expected = 'Tuesday'
        
        # Act
        actual = week(i)
        
        # Assert
        self.assertEqual(expected, actual)
        
    def test_Week_Day3_expectWednesday(self):
        # Arrange
        i = 3
        expected = 'Wednesday'
        
        # Act
        actual = week(i)
        
        # Assert
        self.assertEqual(expected, actual)
    
    def test_Week_Day4_expectThursday(self):
        # Arrange
        i = 4
        expected = 'Thursday'
        
        # Act
        actual = week(i)
        
        # Assert
        self.assertEqual(expected, actual)
        
    def test_Week_Day5_expectFriday(self):
        # Arrange
        i = 5
        expected = 'Friday'
        
        # Act
        actual = week(i)
        
        # Assert
        self.assertEqual(expected, actual)
        
    def test_Week_Day6_expectSaturday(self):
        # Arrange
        i = 6
        expected = 'Saturday'
        
        # Act
        actual = week(i)
        
        # Assert
        self.assertEqual(expected, actual)
        
    def test_Week_Day9_expectInvalid(self):
        # Arrange
        i = 9
        expected = 'Invalid day of week'
        
        # Act
        actual = week(i)
        
        # Assert
        self.assertEqual(expected, actual)
        
    
if __name__ == '__main__':
    unittest.main()