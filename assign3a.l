
%%
[\t ] ;
am|is|are|have|has|can|will|shall|eat|sing|go|goes {
printf("VERB\t %s\n",yytext);}
very|simply|gently { printf("VERB\t %s\n",yytext); }
and|or|also|so|but|if|then {printf("CONJUNCTION\t %s\n",yytext);}
fast|good|honest {printf("ADJECTIVE\t %s\n",yytext);}
I|he|she|we|they|you|this {printf("PRONOUN\t %s\n",yytext);}
in|on|to {printf("PREPOSITION\t %s\n",yytext);}
[a-zA-Z]+ {printf("NOUN\t %s\n",yytext);}
. ;
%%
int main(){
    yylex();
    return 0;
}

int yywrap()
{
    return 0;
}

