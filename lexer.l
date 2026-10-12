
%{
#include <stdio.h>
%}

%%
"let"            { printf("KEYWORD_LET\t%s\n", yytext); }
"print"          { printf("KEYWORD_PRINT\t%s\n", yytext); }
"if"             { printf("KEYWORD_IF\t%s\n", yytext); }
"else"           { printf("KEYWORD_ELSE\t%s\n", yytext); }
"int"            { printf("KEYWORD_INT\t%s\n", yytext); }

[a-zA-Z][a-zA-Z0-9]*  { printf("IDENTIFIER\t%s\n", yytext); }
[0-9]+            { printf("NUMBER\t\t%s\n", yytext); }
\"[^\"\n]*\"      { printf("STRING\t\t%s\n", yytext); }

"="               { printf("ASSIGN\t\t%s\n", yytext); }
"+"               { printf("PLUS\t\t%s\n", yytext); }
"-"               { printf("MINUS\t\t%s\n", yytext); }
"*"               { printf("MULTIPLY\t%s\n", yytext); }
"/"               { printf("DIVIDE\t\t%s\n", yytext); }
"<"               { printf("LESS_THAN\t%s\n", yytext); }
">"               { printf("GREATER_THAN\t%s\n", yytext); }

"{"               { printf("LEFT_BRACE\t%s\n", yytext); }
"}"               { printf("RIGHT_BRACE\t%s\n", yytext); }
"("               { printf("LEFT_PAREN\t%s\n", yytext); }
")"               { printf("RIGHT_PAREN\t%s\n", yytext); }
";"               { printf("SEMICOLON\t%s\n", yytext); }

[ \t\r\n]+        { /* Ignore whitespace */ }
.                 { printf("ERROR\t\t%s\n", yytext); }
%%

int main(void)
{
    printf("TOKEN TABLE\n");
    yylex();
    return 0;
}

int yywrap(void)
{
    return 1;
}
