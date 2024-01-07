from schl import Class_Rooms,School,Subject
from person import Student,Teacher

def main():
    sc=School('amc')
    cl=Class_Rooms('nine')
    sc.Add_classroom(cl)
    sub=Subject('math')
    cl.add_sub(sub)
    
    th=Teacher('mahir')
    sub.add_teacher(th)
    print('hey')
    

if __name__=='__main__':
    main()