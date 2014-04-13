import sys
from pprint import pprint



assignment = dict(
	vector = "PYTHON_LIST",
	double = "double",
	float = "float",
	)

common_data_types = ["int", "float"]

def get_py_type(python_type):
	if "vector" in python_type:
		return assignment["vector"]
	return python_type

def convert_function_to_cpp(data_type):
	if data_type in common_data_types:
		return ""
	if "vector" in data_type:
		return "list_to_vector"

def convert_function_to_py(data_type):
	if data_type in common_data_types:
		return ""
	if "vector" in data_type:
		return "vector_to_list"

def get_container_type(myString):
	return myString[myString.find("<")+1:myString.find(">")]


class Function(object):
	def set_attr(self,attr,value):
		setattr(self,attr,value)

	def get_source(self,source):
		self.source = source.split("\n")

	def get_type(self):
		source = self.source
		return_type = source[0].split(" ")[0]
		self.set_attr("return_type",return_type)	

	def get_name(self):
		source = self.source
		name = source[0].split(" ")[1].split("(")[0].strip()
		self.set_attr("name","_"+name)

	def get_arguments(self):
		source = self.source
		arguments = source[0].split(self.name[1:])[1].strip()[1:][:-1].split(",")
		n = len(arguments)
		new_arguments = []
		for argument in arguments:
			argument = argument.strip().split(" ")
			container_type = None
			if "<" in argument[0]:
				container_type = get_container_type(argument[0])
			curr = dict(
				type = argument[0],
				var = argument[1],
				container_type = container_type
				)
			new_arguments.append(curr)
		self.set_attr("arguments",new_arguments)

	def get_body(self):
		source = self.source
		body = "".join(source[1:])
		self.set_attr("body",body)

	def get_function_call(self):
		call = self.name + "("
		for argument in self.arguments:
			call += argument["var"]+","
		call = call[:-1]
		call += ");"
		self.call = call

	def get_wrapper(self):
		wrapper = ""
		return_type = get_py_type(self.return_type)
		wrapper += return_type + " "+self.name[1:]+ "("
		for argument in self.arguments:
			var = argument["var"]
			data_type = argument["type"]
			wrapper += get_py_type(data_type)+" _"+var+", "

		wrapper = wrapper[:-2] + ")\n{\n" 
		for argument in self.arguments:
			var = argument["var"]
			data_type = argument["type"]
			container_type = argument["container_type"]
			if container_type:
				container_type = "<%s>" % container_type
			else:
				container_type = ""
			wrapper += "	%s %s;\n" % (data_type,var)
			wrapper += "	%s = %s%s(%s);\n" % (var,convert_function_to_cpp(data_type),container_type,"_"+var)
		wrapper += "\n"
		wrapper += "	%s Cpp_result;\n" % (self.return_type)
		wrapper += "	Cpp_result = %s;\n" % self.call 
		wrapper += "	%s Py_result;\n" % get_py_type(self.return_type)
		wrapper += "	Py_result = %s(Cpp_result);\n" % (convert_function_to_py(self.return_type))
		wrapper += "	return Py_result;\n}"
		self.wrapper = wrapper

	def parse(self):
		self.get_type()
		self.get_name()
		self.get_arguments()
		self.get_body()
		self.get_function_call()
		self.get_wrapper()

if __name__ == "__main__":


	source = open("source.cpp","r").readlines()

	#Initialize Function instance
	function = Function()
	function.get_source(source)
	function.get_type()
	function.get_name()
	function.get_arguments()
	function.get_body()
	function.get_function_call()
	function.get_wrapper()

	#pprint(function.return_type)
	#pprint(function.name)
	#pprint(function.arguments)
	#pprint(function.body)
	print(function.wrapper)

	sys.exit()

	
