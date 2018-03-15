class student():
	def __init__(self,stuname,stunum,stuage):
		self.stuname = stuname
		self.stunum  = stunum
		self.stuage  =  stuage
class studentbottom():
	studentlist=[]
class studentleft():
	def tianjia(self):
		print("您选择的是添加学社信息")
		name = input("添加学生姓名")
		num = input("添加学生学号")
		age =input("添加学生性别")
		oldlen=len(studentbottom.studentlist)
		newlist=student(name,num,age)
		studentbottom.studentlist.append(newlist)
		newlen=len(studentbottom.studentlist)
		if newlen-oldlen>0:
			print("添加成功")
			return
	def shanchu(self):
		print("您选择的是删除学生信息")
		num2=input("输入您所需要删除学生的学号")
		k=0
		for i in studentbottom.studentlist:
			if i.stunum==num2:
				del studentbottom.studentlist[k]
				print("删除成功")
				break
			k+=1
			print("查询的学号不存在")	
	def xiugai(self):
		print("您选择的是修改学生信息")
		num3=input('请输入您所需要修改的学生学号')
		for i in studentbottom.studentlist:
			if i.stunum==num3:
				newname=input("输入名字")
				newage=input("输入性别")
				newnum=input("输入学号")
				i.stunum=newnum
				i.stuage=newage
				i.stuname=newname
				print("添加成功")
			else:
				print("您所查询的学号不存在")
	def chaxun(self):
		print("您选择的是查询学生信息")
		num4 = input("输入你所需要查询的学号")
		for i in studentbottom.studentlist:
			if i.stunum==num4:
				print("姓名%s学号%s性别%s"%(i.stuname,i.stunum,i.stuage))
			else:
				print("您所查询的学号不存在")
	def suoyou(self):
		print("您选择的是查询所有学生信息")
		k=0
		for i in studentbottom.studentlist:
			print("姓名\t性别\t学号\t")
			print(i.stuname+"\t"+i.stuage+"\t"+i.stuage)
			if i==len(studentbottom.studentlist)-1:
				break
			k+=1

class view():
	studentnew=studentleft()
	def numxuesheng(self):
		while True:
			print("欢迎使用学生信息管理系统")
			print("请选择：添加1\t删除2\t修改3\t根据学号查询4\t查询所有学生5\t退出exit")
			num=input()
			if num=="1":
				self.studentnew.tianjia()
			elif num=="2":
				self.studentnew.shanchu()
			elif num=="3":
				self.studentnew.xiugai()
			elif num=="4":
				self.studentnew.chaxun()
			elif num=="5":
				self.studentnew.suoyou()


if __name__=="__main__":
	stu1=view()
	stu1.numxuesheng()

