import os
os.system(os.getcwd() + "/core/main")
# import os
# import time
# help_ui = list(open("help.config", "r").read().rstrip())
# print(''.join(help_ui))
# log = open("temp.log", "w")
# log.write("")
# log.close()
# input_ = list(input("Code:\n"))
# valid_mouse = ["1","2","3"]
# valid_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# valid_characters = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
# ]
# output = open("output.py", "a")
# output.write("from ahk import AHK\nahk = AHK()\nimport time\n")
# output.close()
# for i, c in enumerate(input_):
#     output = open("output.py", "a")
#     if c == "+":
#         for n in valid_numbers:
#             if input_[i + 1] == n:
#                 print(f"Waiting {n} second/s")
#                 output.write("time.sleep("+ n +")\n")
#     elif c == "-" and input_[i - 1] in valid_characters:
#         for n in valid_numbers:
#             if input_[i + 1] == n:
#                 print(f"Holding {input_[i - 1]} for {n} second/s")
#                 output.write(f"ahk.key_down('" + input_[i - 1] + "')\n")
#                 output.write("time.sleep("+  n +")\n")
#                 output.write(f"ahk.key_up('" + input_[i - 1] + "')")
#     elif c == "{" and input_[i + 1] in valid_mouse:
#         n = input_[i + 1]
#         if n == "1":
#           print(f"Pressed mouse1")
#           output.write("ahk.click()\n")
#         elif n == "2":
#           print(f"Pressed mouse2")
#           output.write("ahk.right_click()\n")
#         elif n == "3":
#           print(f"Mouse3 is currently not supported")
#     elif c == "!" and input_[i + 1] in valid_characters:
#         print(f"Pressing {input_[i + 1]}")
#         output.write(f"ahk.key_press('" + input_[i + 1] + "')\n")
#     elif c == "#":
#       string = input("string: ")
#       print(f"Typing {string}")
#       output.write("ahk.type('"+ string +"')\n")
#     elif c == "/":
#       x = input("X: ")
#       y = input("Y: ")
#       print(f"Moving mouse to {x} {y}")
#       output.write(f"ahk.mouse_position = (" + x + ", "+ y +")")
#     else:
#         log = open("temp.log", "a")
#         log.write(f"possible error at character {i + 1}\n{input_}\n")
#         log.close()
#     output.close()
# def build():
#         output.close()
#         os.system("python build.py build")
#         print("Macro has been compiled")
#         print("Check " + os.getcwd() + "/build/exe.*-3.7 for a file named output")
# print("Starting compiler in 3")
# time.sleep(1)
# print("Starting compiler in 2")
# time.sleep(1)
# print("Starting compiler in 1")
# time.sleep(1)
# build()