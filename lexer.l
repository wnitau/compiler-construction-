%{
#include <stdio.h>
%}

%option noyywrap

%%

"let"       { printf("KEYWORD: %s\n", yytext); }
"print"     { printf("KEYWORD: %s\n", yytext); }
"if"        { printf("KEYWORD: %s\n", yytext); }

[a-zA-Z][a-zA-Z0-9]*  { printf("IDENTIFIER: %s\n", yytext); }

[0-9]+      { printf("NUMBER: %s\n", yytext); }

"="         { printf("OPERATOR: %s\n", yytext); }
"+"         { printf("OPERATOR: %s\n", yytext); }
"-"         { printf("OPERATOR: %s\n", yytext); }
"*"         { printf("OPERATOR: %s\n", yytext); }
"/"         { printf("OPERATOR: %s\n", yytext); }
"<"         { printf("OPERATOR: %s\n", yytext); }
">"         { printf("OPERATOR: %s\n", yytext); }

{}();     { printf("DELIMITER: %s\n", yytext); }

[ \t\r\n]+  { /* Ignore whitespace */ }

.           { printf("UNKNOWN: %s\n", yytext); }

%%
int main(void)
{
    yylex();
    return 0;
}