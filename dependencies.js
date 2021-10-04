var dependencyTree = require('dependency-tree');

// Returns a dependency tree object for the given file
var tree = dependencyTree.toList({
    filename: './src/app/whatever',
    directory: './src',
});

console.log(tree);
