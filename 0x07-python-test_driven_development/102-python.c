#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	printf("  type:");

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf(" compact ascii\n");
	}
	else if (PyUnicode_IS_COMPACT(p))
	{
		printf(" compact unicode object\n");
	}

	printf("  length: %d\n", (int)PyUnicode_GET_LENGTH(p));
	printf("  value: ");
	PyObject_Print(p, stdout, 1);
	putchar('\n');
}
