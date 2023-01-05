# teenytinycompiler

This is an exercise to __rebuild__ a simple compiler that implement a dialect of BASIC. All code here is copied from the following awesome notes of Austin Henley [posts](https://austinhenley.com/blog/teenytinycompiler1.html)/[github repo](https://github.com/AZHenley/teenytinycompiler). Although the majority of the code is the same as the mentioned repository, this is not an identical replica of the code/repo. Some changes compared to the original post are the followings:
- Explicit tests are provided (found in `tests` folder).
- Occasional refactoring as well as python sepcific data structures when it is appropriate. 
- Some aspects of the language might have been expanded. 
- Structure of the code is different from the repository, since I have followed the blog posts instead of the code in the repository. 
- Extra methods or functions that could help with debugging.

## Ideas for extension and modifications
Use the ideas and implementation from David Callanan to write an AST for the parser (or rewrite the parser completely based on his code). Look for additional details to [youtube](https://www.youtube.com/playlist?list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD) posts and accompanying [github](https://github.com/davidcallanan/py-myopl-code) source. 