#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_COL 65536

char findTheDifference(char* s, char* t) {
    while (*s == *t) {
        s++;
        t++;
    }

    while (*s == '\"')
        s++;
    while (*t == '\"')
        t++;

    if (*s != '\0')
        return *s;
    else if (*t != '\0')
        return *t;
    else
        return '\0';
}

void print_char(char *s)
{
    while (*s != '\0') {
        printf("%02x ", *s++);
    }
    printf("\n");
}

void loop_main(char *s, char *t)
{
    // char s[] = "abcd", t[] = "abcde";
    
    printf("s = %s, t = %s\n", s, t);
//  print_char(s);
//  print_char(t);

    printf("%c\n", findTheDifference(s, t));
}

int main(int argc, char *argv[])
{
    if (argc < 2) {
        printf("Usage: %s <testdata.txt>\n", argv[0]);
        return 0;
    }

    FILE *fp;
    char readline[MAX_COL];
    char *s, *t;
    int readline_length;

    if ((fp = fopen(argv[1], "r")) == NULL) {
        fprintf(stderr, "%s\n", argv[1]);
        exit(EXIT_FAILURE);
    }

    while ( fgets(readline, MAX_COL, fp) != NULL ) {
    //    printf("%s", readline);
        if ((readline_length = strlen(readline)) > 0) {
            if (readline[readline_length - 1] == 0x0a) {
                readline[readline_length - 1] = '\0';
            }
            if (readline[readline_length - 2] == 0x0d) {
                readline[readline_length - 2] = '\0';
            }
        }

        s = strtok(readline, ",");
        t = strtok(NULL, ",");
        loop_main(s, t);
    }

    /*
    while ( fscanf(fp, "\"%s\",\"%s\"", s, t) != EOF ) {
        printf("s = %s, t = %s\n", s, t);
        loop_main(s, t);
    }
    */
    fclose(fp);

    return 1;
}
