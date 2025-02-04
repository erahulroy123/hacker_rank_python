if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    students.sort(key = lambda student: student[1])
    
    second_lowest_num = students[0][1]
    for student in students:
        if student[1] > second_lowest_num:
            second_lowest_num = student[1]
            break
            
    second_lowest_names = [student[0] for student in students if student[1] == second_lowest_num] 
    
    second_lowest_names.sort()
    
    for name in second_lowest_names:
        print(name)
            
