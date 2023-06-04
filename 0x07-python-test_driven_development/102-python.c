#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (!PyUnicodeCheck(p))
	{
		printf("  [ERROR] Invalid String Object\n");
	}

	printf("  type:");

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf(" compact ascii\n");
	}
	if (PyUnicode_IS_COMPACT(p))
	{
		printf(" compact unicode object\n")
	}

	printf("  length: %d\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %s\n", PyObject_Print(p, stdout, 1));
}
