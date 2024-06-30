#exercise
print('Time calculator'.center(55,'-'))
import time
timecalculate=time.strftime('%H:%M:%S')
print(timecalculate)#it gives the time of country according to pakistan
# timecalculate=time.strftime('%H')
# print(timecalculate)
# timecalculate=time.strftime('%M')
# print(timecalculate)
# timecalculate=time.strftime('%S')
# print(timecalculate)
if (timecalculate>='00:00:00' and timecalculate<='11:59:59'):
  print('Good Morning')
elif (timecalculate>='12:00:00' and timecalculate<='16:59:59'):
  print('Good Afternoon')
elif (timecalculate>='17:00:00' and timecalculate<='20:59:59'):
  print('Good Evening')
else:
  print('Good Night')
  




