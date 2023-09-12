#!/usr/bin/node
function fun (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
exports.callMeMoby = fun;
