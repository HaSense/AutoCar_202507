class Student:
    #학번(stnum), 이름(name), 전공(major)
    #stnum : int
    def __init__(self, stnum, name, major):
        self.stnum = stnum
        self.name = name
        self.major = major
    #멤버 메소드
    def study(self):
        print('공부하다')
    
    def majorStudy(self, majorClass):
        print(f'{majorClass}을/를 공부하다.')
    
    def eat(self):
        return '먹다'
    
if __name__ == '__main__':
    tomi = Student(1, '토미', '전자공학')
    print(f'이름 : {tomi.name}, 학번 : {tomi.stnum}, 전공 : {tomi.major}')
    tomi.study()
    tomi.majorStudy('전자기학')
    print(tomi.eat())
