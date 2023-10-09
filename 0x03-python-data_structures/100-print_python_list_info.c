#include <Python.h>
/**
 * print_python_list_info - prints some basic info about python lists
 *
 * @p: a PyObject list
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	int i, size, buff;

	size = Py_SIZE(p);
	buff = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", buff);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_Type(obj)->tp_name);
	}
}
