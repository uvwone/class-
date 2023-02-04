import random

class RSP:
      def __init__(self):
            self.player = ''
            self.computer = ''
            self.player_win_count = 0
            self.computer_win_count = 0
            self.case = ['가위', '바위', '보']

      def Start(self):
            while True:
                  self.game_input()
                  rst = self.game_calculate()
                  self.print_who_wins(rst)
                  if self.print_finally_win():
                        break
      def game_input(self):
            while True:
                  pl = input('가위 바위 보 중 입력하세요 : ')
                  if (not pl.isalpha()) and pl not in self.case:
                        print('잘못 입력하셨습니다. 다시 입력하세요.')
                        continue
                  else:
                        self.player = pl
                        break
            self.computer = random.choice(self.case)
            return

      def game_calculate(self):
            result = 0
            if self.player == self.computer:
                  return result
            if self.player == self.case[0]:
                  if self.computer == self.case[1]:
                        self.computer_win_count+=1
                        result = 1
                  elif self.computer == self.case[2]:
                        self.player_win_count+=1
                        result = 2
            if self.player == self.case[1]:
                  if self.computer == self.case[0]:
                        self.player_win_count+=1
                        result = 2
                  elif self.computer == self.case[2]:
                        self.computer_win_count+=1
                        result = 1
            if self.player == self.case[2]:
                  if self.computer == self.case[0]:
                        self.computer_win_count+=1
                        result = 1
                  elif self.computer == self.case[1]:
                        self.player_win_count+=1
                        result = 2
            return result
      def print_who_wins(self, result):
            if result == 0:
                  print('비김')
            elif result == 1:
                  print('컴퓨터 승')
            elif result == 2:
                  print('플레이어 승')

      def print_finally_win(self):

            if self.player_win_count >= 3:
                  print('플레이어 최종 승리')
                  return 1
            elif self.computer_win_count >= 3:
                  print('컴퓨터 최종 승리')
                  return 1
            return 0
if __name__ == '__main__':
      rsp = RSP()
      rsp.Start()
