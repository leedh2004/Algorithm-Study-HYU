import sys

def DpByrgb(firstColorIdx):
  dp = [[ 1000001 for _ in range(3)] for _ in range(n)]
  dp[0][firstColorIdx] = color[0][firstColorIdx]

  # 전체 방 갯수만큼 순회
  for n_idx in range(1,n):

    # 현재 색상
    for color_idx in range(3):
      
      # 1칸 전 색상
      for compare_idx in range(3):
        
        # 색상이 같은 경우 - 무시
        if color_idx==compare_idx:
          continue
        
        # 색상이 다른 경우 - 점화식 적용
        else : 
          dp[n_idx][color_idx] = min(dp[n_idx][color_idx],dp[n_idx-1][compare_idx]+color[n_idx][color_idx])

  ans = 1000001

  # 최소값 찾기
  for i in range(3):
    # 첫방과 미지막방 예외처리
    if i==firstColorIdx:
      continue
    ans = min(ans,dp[n-1][i])

  return ans

n = int(sys.stdin.readline())
color = []
for i in range(n):
  tmp = list(map(int,sys.stdin.readline().split()))
  color.append(tmp)

ans = min(DpByrgb(0),DpByrgb(1),DpByrgb(2))
print(ans)

