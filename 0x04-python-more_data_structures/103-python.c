#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

void print_python_list(PyObject *p)
{
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", (int)PyList_GET_SIZE(p));
	printf("[*] Allocated = %d\n", (int)((pyListObject *)p)->allocated);

	for (i = 0; i < (int)PyList_GET_SIZE(p); i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);

		printf("Element %d: %s\n", i, (char *)PyObject_Type(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	int i;

	printf("[.] bytes object info\n");
	printf("  size: %d\n", (int)PyBytes_Size(p));

	const char *str = PyBytes_AS_STRING(p);
	printf("  trying string: %s\n", str);

	if ((int)PyBytes_Size(p) < 10)
	{
		i = (int)PyBytes_Size(p) + 1
	}
	else
	{
		i = 10
	}

	printf("  first %d bytes: ", i);

	for (i = 0; i < (int)PyBytes_Size(p) + 2; i++)
	{
		printf(" %02x", str[i]);
	}
	putchar('\n');
}
