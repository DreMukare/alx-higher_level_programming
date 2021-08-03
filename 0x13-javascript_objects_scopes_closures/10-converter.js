#!/usr/bin/node
exports.converter = function (base) {
  return (args) => args.toString(base);
};
