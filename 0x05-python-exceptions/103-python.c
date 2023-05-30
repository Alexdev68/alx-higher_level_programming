#include <Python.h>
#include <stdio.h>
#include <string.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
	int i;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %d\n", (int)PyList_GET_SIZE(p));
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

	for (i = 0; i < (int)PyList_GET_SIZE(p); i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);

		printf("Element %d: %s\n", i, (char *)(item)->ob_type->tp_name);

		if (strcmp((char *)(item)->ob_type->tp_name, "bytes") == 0)
		{
			print_python_bytes(item);
		}
		if (strcmp((char *)(item)->ob_type->tp_name, "float") == 0)
		{
			print_python_float(item);
		}
	}
	fflush(stdout);
}

void print_python_bytes(PyObject *p)
{
	int i, j;
	PyObject *strObj = PyObject_Str(p);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %d\n", (int)PyBytes_Size(p));

	const char *str = PyUnicode_AsUTF8(strObj);
	if (str == NULL)
	{
		return;
	}
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
	fflush(stdout);
}

void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %f", (double)PyFloat_AsDouble(p));
	fflush(stdout);
}
