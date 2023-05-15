#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
        Py_ssize_t i;

        printf("[*] Size of the Python List = %d\n", (int)Py_SIZE(p));
        printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

        for (i = 0; i < Py_SIZE(p); i++)
        {
                PyObject *item = PyList_GetItem(p, i);

                printf("Element %d: %s\n", (int)i, (char *)Py_TYPE(item)->tp_name);
        }
}
