import unittest
from turtle import Screen
from src.turtleforbeginners import draw_cloud, sun, meer




class TestTurtleFunctions(unittest.TestCase):

    def setUp(self):
        # Create a screen instance to handle turtle graphics
        self.screen = Screen()
        self.screen.setup(width=600, height=600)

    def test_draw_cloud(self):
        # Call the draw_cloud function with the parameters
        draw_cloud(0, 0, 50, "white")
        # You can add assertions here to check if the cloud is drawn correctly

    def test_sun(self):
        # Call the sun function with test parameters
        sun(0, 100, 12)
        # Add assertions to check if the sun is drawn correctly

    def test_meer(self):
        # Call the meer function
        meer()
        # Add assertions to check if the sea is drawn correctly

    def tearDown(self):
        # Close the turtle screen after tests
        self.screen.bye()


if __name__ == "__main__":
    unittest.main()
    test_sun()