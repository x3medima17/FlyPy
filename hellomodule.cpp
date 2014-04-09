#include <iostream>
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/python/list.hpp>
#include <boost/python/extract.hpp>
#include "utils.h"
#include <string>

using namespace std;
void say_hello(string name)
{
	cout<<"Hello "<<name<<" !\n";
}

void print_list(boost::python::list &L)
{
	VECTOR_OF_INTS V;
	V = list_to_vector(L);
	for(size_t i=0; i<V.size();i++)
		cout<<V[i]<<" ";
	cout<<endl;
}

PYTHON_LIST bsort(PYTHON_LIST &L)
{
	VECTOR_OF_INTS V;
	V = list_to_vector(L);
	size_t n = V.size();
	for(size_t i=0;i<n;i++)
		for(size_t j=0;j<n;j++)
			if(V[i]<V[j])
				swap(V[i],V[j]);
	L = vector_to_list(V);
	return L;

}

using namespace boost::python;

BOOST_PYTHON_MODULE(hello)
{
	def("say_hello",say_hello);
	def("print_list",print_list);
	def("bsort",bsort);
}
