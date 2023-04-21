import numpy as np

# fname='test_input.txt'
fname='input.txt'

this_count = 0
max_count1 = 0
max_count2 = 0
max_count3 = 0

this_elf = 1
max_elf1 = 0
max_elf2 = 0
max_elf3 = 0


with open(fname) as fp:
    for line in fp:
        stripped = str.strip(line)
        if stripped == '':
            if this_count>max_count1:
                max_count3=max_count2
                max_elf3=max_elf2

                max_count2=max_count1
                max_elf2=max_elf1

                max_count1=this_count
                max_elf1=this_elf
                print(f'new top 1: {this_count}({this_elf})')
                print(f'1:{max_count1}({max_elf1}) 2:{max_count2}({max_elf2}) 3:{max_count3}({max_elf3})')
            elif this_count>max_count2:
                max_count3=max_count2
                max_elf3=max_elf2

                max_count2=this_count
                max_elf2=this_elf

                print(f'new top 2: {this_count}({this_elf})')
                print(f'1:{max_count1}({max_elf1}) 2:{max_count2}({max_elf2}) 3:{max_count3}({max_elf3})')

            elif this_count>max_count3:
                max_count3=this_count
                max_elf3=this_elf

                print(f'new top 3: {this_count}({this_elf})')
                print(f'1:{max_count1}({max_elf1}) 2:{max_count2}({max_elf2}) 3:{max_count3}({max_elf3})')   
                # max_count3=this_count
                # max_elf3=this_elf
                
                # print('>3', max_count3,max_elf3)


                # if max_count2>max_count3:

                #     buff_count = max_count2
                #     buff_elf = max_elf2
                #     max_count2=max_count3
                #     max_elf2=max_elf3
                #     max_count3=buff_count
                #     max_elf3=buff_elf

                #     print('>2', max_count2,max_elf2)
                
                        
                #     if max_count1>max_count2:
                #         buff_count = max_count1
                #         buff_elf = max_elf1
                #         max_count1=max_count2
                #         max_elf1=max_elf2
                #         max_count2=buff_count
                #         max_elf2=buff_elf

                        
                #         print('>1', max_count1,max_elf1)

            this_elf+=1
            this_count=0
        else:
            this_count+=int(stripped)
print(max_count1,max_count2,max_count3,max_count1+max_count2+max_count3)