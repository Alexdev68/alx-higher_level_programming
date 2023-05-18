#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

void print_python_list(PyObject *p)
{
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", (int)PyList_GET_SIZE(p));
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

	for (i = 0; i < (int)PyList_GET_SIZE(p); i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);

		printf("Element %d: %s\n", i, (char *)(item)->ob_type->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	int i;
	int j;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}

	printf("  size: %d\n", (int)PyBytes_Size(p));

	const char *str = PyBytes_AS_STRING(p);
	printf("  trying string: %s\n", str);

	if ((int)PyBytes_Size(p) < 10)
	{
		i = (int)PyBytes_Size(p) + 1;
	}
	else
	{
		i = 10;
	}

	printf("  first %d bytes:", i);

	for (j = 0; j < i; j++)
	{
		printf(" %02hhx", str[j]);
	}
	putchar('\n');
}
