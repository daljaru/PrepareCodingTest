#큰 수의 법칙

'''
다양한 수의 배열이 주어질 때 주어진 수들을 M번 더하여 가장 큰수를 만들어보시오. 
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수는 없다.

예를 들어 2,4,5,4,6이라면 M이 8이고 K가 3이라고 가정하면
큰 수의 법칙에 의해 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 가 가장 큰 수가 된다. 
'''
if __name__ == '__main__':
  num_array = [2,4,5,4,6]
  num_array.sort()
  print(num_array)
  alpha = num_array[-1]
  beta = num_array[-2]
  m = 8
  k = 3

  result = (alpha*k + beta) * (m // (k + 1)) + (alpha * m % (k + 1))
  print(result)

