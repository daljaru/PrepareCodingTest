
if __name__ == '__main__':
  # 일차원 리스트
  list_comp1 = [i for i in range(10)]
  print(list_comp1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  list_comp2 = [i*i for i in range(10)]
  print(list_comp2) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

  #이차원 리스트
  # N * M 크기의 이차원 리스트.
  N = 3
  M = 4

  list_comp3 = [[0] * M for i in range(N)]
  print(list_comp3) #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
  

  origin_list = [1,2,3,4,5,6,7,4,3,5,3,4,3]
  remove_set = [3, 4]
  list_comp4 = [i for i in origin_list if i not in remove_set]
  print(list_comp4)