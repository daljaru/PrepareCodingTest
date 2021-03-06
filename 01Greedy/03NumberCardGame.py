# 숫자 카드 게임
#여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
'''
숫자가 쓰인 카드들이 N * M 형태로 놓여 있다. 
N은 행의 개수. M은 열의 개수이다. 
먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다. 
선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮으 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다. 

'''

result = -1
if __name__ == '__main__':
  N, M = map(int, input().split())
  for i in range(N):
    arr = list(map(int, input().split()))
    min_number = min(arr)
    result = max(result, min_number)

  print(result)