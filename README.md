USAGE:

    ./clean_h  <file header name>

    You can add '-CSFML' to have SFML includes

FLAGS:

    -CSFML -> add CSFML libraries includes
    -u -> update a .h which already exist

GOAL:

    Create a header file already prepared in your 'include' folder.
    If you don't choose any name, your .h will be named 'my.h'.
    Lot of includes are already set and the src folders's prototypes functions are set too.

YOU MUST HAVE:

    A folder named 'src' which contains all your .c files.
    A folder names 'include'.