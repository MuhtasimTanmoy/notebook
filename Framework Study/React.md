There are 3 possibilities to store state:
- Component
- Context API
- Redux
Personally, I use component (useState) when the state is local or it is shared with only children.
When it is very localized and makes sense to do it (like an aggregate in DDD terms or with a few levels of nesting), then going for Context API makes lot of sense.
When state is shared among far away parts of the program, then Redux makes more sense.
Talking about performance, I also once read someone saying "Redux for high-frequency (>1 second) state changes, Context API for low-frequency changes".