import sys
import os

# Add the parent directory of 'console_wind' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from console_wind.sub_screens import SubScreen
from console_wind.console_screen import ConsoleScreen

# import sys
# print(sys.path)



layout = [SubScreen(3, 2), SubScreen(4, 3), SubScreen(30, 10)]


cs = ConsoleScreen(layout, 199, 230)

print(cs)
for i in cs.sub_screens:
    i.display_content()
    print("\n")