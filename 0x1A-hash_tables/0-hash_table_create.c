#include <stdlib.h>
#include "hash_tables.h"

typedef struct hash_table {
    unsigned long int size;
    int *array;
} hash_table_t;

hash_table_t *hash_table_create(unsigned long int size) {
    if (size < 1) {
        return NULL;
    }
    hash_table_t *hash_table = malloc(sizeof(hash_table_t));
    if (hash_table == NULL) {
        return NULL;
    }
    hash_table->size = size;
    hash_table->array = malloc(size * sizeof(int));
    if (hash_table->array == NULL) {
        free(hash_table);
        return NULL;
    }
    for (unsigned long int i = 0; i < size; i++) {
        hash_table->array[i] = 0;
    }
    return hash_table;
}
