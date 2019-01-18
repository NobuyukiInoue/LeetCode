#include <stdlib.h>
#include <string.h>

/* Function prototype declaration */
void replace(char *buf, const char *str1, const char *str2);
int split( char *str, const char *delim, char *outlist[] );


int split( char *str, const char *delim, char *outlist[] )
{
    char    *pos1, *pos2;
    char    *temp_str, *dst;
    int     cnt = 0;
    int     MAXITEM = 256;

    pos1 = str;
    pos2 = strstr( pos1, delim );
    while( pos2 != NULL && cnt < MAXITEM ) {
        temp_str = malloc(sizeof(char) * 256);
        dst = temp_str;

        while ( pos1 < pos2 )
            *dst++ = *pos1++;
        *dst = '\0';

        outlist[cnt++] = temp_str;
        pos1 = pos2 + strlen(delim);
        pos2 = strstr( pos1, delim );
    }

    temp_str = malloc(sizeof(char) * 256);
    dst = temp_str;

    while ( *pos1 != '\0')
        *dst++ = *pos1++;
    *dst = '\0';
    outlist[cnt++] = temp_str;

    return cnt;
}


void replace(char *buf, const char *str1, const char *str2)
{
    char tmp[1024 + 1];
    char *p;

    while ((p = strstr(buf, str1)) != NULL) {
        /* 見つからなくなるまで繰り返す
            pは旧文字列の先頭を指している */
        if (*str2 != '\0') {
            *p = '\0'; /* 元の文字列を旧文字列の直前で区切って */
            p += strlen(str1);  /* ポインタを旧文字列の次の文字へ */
            strcpy(tmp, p);     /* 旧文字列から後を保存 */
            strcat(buf, str2);  /* 新文字列をその後につなぎ */
            strcat(buf, tmp);   /* さらに残りをつなぐ */
        } else {
            char *src, *dst;
            src = dst = p;

            *src = '\0'; /* 元の文字列を旧文字列の直前で区切って */
            dst += strlen(str1);  /* ポインタを旧文字列の次の文字へ */
            while (*dst != '\0') {
                *src++ = *dst++;
            }
            *src = '\0';
            p += strlen(str1);
        }
    }
}
