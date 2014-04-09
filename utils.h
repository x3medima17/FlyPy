#include <vector>
#include <boost/python/list.hpp>
#include <boost/python/extract.hpp>

using namespace std;

typedef vector<int> VECTOR_OF_INTS;
typedef boost::python::list PYTHON_LIST;

VECTOR_OF_INTS list_to_vector(PYTHON_LIST &L)
{
	VECTOR_OF_INTS V;
	for(int i=0; i<len(L);i++)
	{
		int k = boost::python::extract<int>(L[i]);
		V.push_back(k);
	}
	return V;
}

PYTHON_LIST vector_to_list(VECTOR_OF_INTS &V)
{
	PYTHON_LIST L;
	size_t n = V.size();
	for(size_t i = 0; i<n; i++)
		L.append(V[i]);
	return L;
}


