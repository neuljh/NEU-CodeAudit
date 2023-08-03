#include <stdio.h>
#include <string.h>

int main() {
    // strcpy: Copy one string to another
    char src[] = "Hello, world!";
    char dest[20];
    strcpy(dest, src);
    printf("strcpy: %s\n", dest);

    // strcat: Concatenate two strings
    char str1[50] = "Hello";
    char str2[] = " World!";
    strcat(str1, str2);
    printf("strcat: %s\n", str1);

    // sprintf: Format and store a series of characters in a string
    char buffer[50];
    int num = 42;
    sprintf(buffer, "The answer is %d", num);
    printf("sprintf: %s\n", buffer);

    // memcpy: Copy a block of memory from one location to another
    char src_array[] = "Copy me!";
    char dest_array[20];
    memcpy(dest_array, src_array, strlen(src_array) + 1);
    printf("memcpy: %s\n", dest_array);

    return 0;
}
