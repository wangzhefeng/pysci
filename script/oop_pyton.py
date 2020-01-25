#!/usr/bin/env python
# -*- coding: utf-8 -*-


class FirstClass(object):
	def setdata(self, value):
		self.name = value

	def display(self):
		print(self.name)



class SecondClass(FirstClass):
	def display(self):
		print("Current value = %s" % self.data)



def main():
	x = FirstClass()
	y = FirstClass()
	x.setdata("wangzhefeng")
	y.setdata(3.14159)
	x.display()
	y.display()

	x.data = "New Value"
	x.display()

	x.anothername = "spam"



if __name__ == "__main__":
	main()