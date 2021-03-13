#1이 될 때까지
'''
어떤 수 N이 1일 될 때가지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 단 두번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다. 
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
'''

if __name__ == '__main__':
  number, alpha = map(int, input().split())
  count = 0
  while(True):
    if((number % alpha) != 0):
      number -= 1
      count += 1
    if number == 1:
      break
    if((number % alpha) == 0):
      number /= alpha
      count += 1
    if number == 1:
      break

  print(count)