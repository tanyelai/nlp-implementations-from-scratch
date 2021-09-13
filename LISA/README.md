## About ELIZA

        User: I am unhappy.
        ELIZA: DO YOU THINK COMING HERE WILL HELP YOU NOT TO BE UNHAPPY
        User: I need some help, that much seems certain.
        ELIZA: WHAT WOULD IT MEAN TO YOU IF YOU GOT SOME HELP
        User: Perhaps I could learn to get along with my mother.
        ELIZA: TELL ME MORE ABOUT YOUR FAMILY
        User: My mother takes care of me.
        ELIZA: WHO ELSE IN YOU FAMILY TAKES CARE OF YOU
        User: My father.
        ELIZA: YOUR FATHER
        User: You are like my father in some ways.

> The dialog above is from ELIZA, an early natural language processing system that could continue on a limited conversation with a user by imitating the responses
of a Rogerian psychotherapist ( Weizenbaum, 1966 ).\
*"Speech and Language Processing"*

<\b>
ELIZA is amazingly simple program that uses pattern matching to link phrases together like "I need X" and translate them into appropriate outputs like 
"What would it mean to you if you got X". This basic idea succeeds in this domain because ELIZA does not actually need to know anything to mimic a Rogerian psychotherapist.

<\b>
## About LISA

Substitutions and capture groups are very useful in implementing simple chatbots like ELIZA.
<\b>
<\b>
Eliza works by having a series or cascade of regular expression substitutions each of which matches and changes some part of the input lines. The first substitutions then
change all instances of "my" to "your", and "I'm" to "You are" and so on. The next set of substitutions matches and replaces other patterns in the input.
