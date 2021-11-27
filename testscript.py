import msvcrt
import time
def raw_input_with_timeout(prompt, timeout=5.0):
  print(prompt)
  finishat = time.time() + timeout
  result=[]
  while True:
    if msvcrt.kbhit() == True:
      result = result.append(msvcrt.getch())
      if result == []:  # or \n, whatever Win returns;-)
        break
      time.sleep(0.1)  # just to yield to other processes/threads
    else:
      if time.time() > finishat:
        break

raw_input_with_timeout("hi")
print("end")