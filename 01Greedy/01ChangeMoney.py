# 거스름 돈 거르기.
'''
거스름돈이 1260원이다. 당신에게 무한히 많은 500원, 100원, 50원, 10원 동전들이 있다면 거슬러 줄 수 있는 동전의 최소 개수를 구하시오.
'''


if __name__ == '__main__':
  total_change = 1260 #거스름돈
  moneys = [500, 100, 50, 10] # 동전 종류
  count = 0 #최소 동전 개수

  # 동전 종류 중에서   
  for money in moneys:

    #현재 동전으로 몇 개를 내야할까
    count += total_change // money

    #나머지를 다시 거스름돈으로 갱신
    total_change = total_change % money
  
  print(count)