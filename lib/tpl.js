/*
 * tpl.js
 * micro javascript template, which can be converted to bottle.py style template automatically.
 * so that frontside(js) and backside(python) web development can be separated clearly.
 *
 * TEMPLATE IS PROTOTYPE
 *
 * Author: Panda Xiong
 * License: MIT
 */
(function() {
    this.tmpl = function (str, data) {
        var cache = {};
        return cache[str] = cache[str] || new Function("data",
            "var out=''; with(data){out+='"
           +document.getElementById(str).innerHTML
           .replace(/[\r\t\n]/g, " ")
           .replace(/'(?=[^%]*%>)/g,"\t")
           .split("'").join("\\'")
           .split("\t").join("'")
           .replace(/<%=(.+?)%>/g, "'; out += $1; out += '")
           .split("<%").join("';")
           .split("%>").join("out+='")
           +"';} return out;");
    };
    this.tpl = function () {
        this.tpl = {};
        var es = document.getElementsByTagName("script");
        for (e in es) {
            var id = es[e].id;
            if (id && (id.indexOf("tpl.") == 0))
                this.tpl[id.substr(4)] = this.tmpl(id);
        }
    };
})();