%%
[ \t]+   ;
public |
private |
protected   {printf("%s : This is access specifier\n",yytext);}
for |
while |
if  {printf("%s : This is structure keywords\n",yytext);}
class |
static |
void    {printf("%s : This is keywords\n",yytext);}
"{" |
"}" |
"(" |
")"     {printf("%s : This is brackets\n",yytext);}
"+" |
"-" |
"*" |
"/"     {printf("%s : This is arithmatic operator\n",yytext);}
"!" |
"&&" |
"||" {printf("%s : This is logical operator\n",yytext);}
"int"	|
"float"	|
"char"	|
"string"	{printf("%s : This is data types\n",yytext);}
[a-zA-z][a-zA-Z0-9]*     {printf("%s : This is variable\n",yytext);}
[0-9]+  |
[0-9]+.[0-9]+ |
.[0-9] {printf("%s : This is number",yytext);}
%%

int main(){
    yylex();
    return 0;
}

int yywrap()
{
    return 0;
}
