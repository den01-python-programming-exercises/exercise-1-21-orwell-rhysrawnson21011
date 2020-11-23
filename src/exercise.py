def main():
    orwell = 1984
    
    while True:
      guess = int(input('what is the orwell?:'))
      if guess != orwell:
        print('not orwell')
      if guess == orwell: 
        print('orwell ')
        break
if __name__ == '__main__':
    main()
