// CodeMirror, copyright (c) by Marijn Haverbeke and others
// Distributed under an MIT license: http://codemirror.net/LICENSE

(function(mod) {
  if (typeof exports == "object" && typeof module == "object") // CommonJS
    mod(require("../../lib/codemirror"));
  else if (typeof define == "function" && define.amd) // AMD
    define(["../../lib/codemirror"], mod);
  else // Plain browser env
    mod(CodeMirror);
})(function(CodeMirror) {
  "use strict";

  function errorIfNotEmpty(stream) {
    var nonWS = stream.match(/^\s*\S/);
    stream.skipToEnd();
    return nonWS ? "error" : null;
  }

  CodeMirror.defineMode("riscv", function(e, t) {
    function r(e, t) {
        return new RegExp("^(?:" + e.join("|") + ")$", t)
    }
    var n = r(["add", "addi", "and", "andi", "auipc", "beq", "bge", "bgeu", "blt", "bltu", "bne", "div", "divu", "ecall", "jal", "jalr", "lb", "lbu", "lh", "lhu", "lui", "lw", "mul", "mulh", "mulhsu", "mulhu", "or", "ori", "rem", "remu", "sb", "sh", "sll", "slli", "slt", "slti", "sltiu", "sltu", "srai", "srl", "srli", "sub", "sw", "xor", "xori", "beqz", "bgez", "bgt", "bgtu", "bgtz", "ble", "bleu", "blez", "bltz", "bnez", "call", "jal", "jalr", "j", "jr", "la", "lb", "lbu", "lh", "lhu", "li", "lw", "mv", "neg", "nop", "ret", "not", "ret", "sb", "seqz", "sgtz", "sh", "sltz", "snez", "sw", "tail", "seq", "sge", "sgeu", "sgt", "sgtu", "sle", "sleu", "sne"], "i"),
        i = r(["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12", "x13", "x14", "x15", "x16", "x17", "x18", "x19", "x20", "x21", "x22", "x23", "x24", "x25", "x26", "x27", "x28", "x29", "x30", "x31", "zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2", "s0", "s1", "a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "t3", "t4", "t5", "t6"], ""),
        o = r([".data", ".text", ".globl", ".float", ".double", ".asciiz", ".word", ".byte"], "i");

    function l(e, t) {
        var r = e.next();
        if ("#" == r) return e.skipToEnd(), "comment";
        if ('"' == r || "'" == r) return t.cur = (n = r, function(e, t) {
            for (var r, i = !1; null != (r = e.next()) && (r != n || i);) i = !i && "\\" == r;
            return i || (t.cur = l), "string"
        }), t.cur(e, t);
        var n;
        return /\d/.test(r) ? (e.eatWhile(/[\w.%]/), "number") : /[.\w_]/.test(r) ? (e.eatWhile(/[\w\\\-_.]/), "variable") : null
    }
    return {
        startState: function(e) {
            return {
                basecol: e || 0,
                indentDepth: 0,
                cur: l
            }
        },
        token: function(e, t) {
            if (e.eatSpace()) return null;
            var r = t.cur(e, t),
                l = e.current();
            return "variable" == r && (o.test(l) ? r = "keyword" : n.test(l) ? r = "builtin" : i.test(l) && (r = "variable-2")), r
        }
    }
});

  CodeMirror.defineMIME("application/pgp", "asciiarmor");
  CodeMirror.defineMIME("application/pgp-encrypted", "asciiarmor");
  CodeMirror.defineMIME("application/pgp-keys", "asciiarmor");
  CodeMirror.defineMIME("application/pgp-signature", "asciiarmor");
});
