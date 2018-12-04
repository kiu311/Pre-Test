function createArrayOfFunctions(y) {
  var array = [];
  for (let i = 0; i < y; i++) {
    array[i] = function (x) {
      return x + i;
    }
  }
  return array;
}
