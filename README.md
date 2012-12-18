# tpl.js #

*TEMPLATE IS PROTOTYPE*

 This is a micro javascript template, which can be converted to bottle.py style template automatically. so that frontside(js) and backside(python) web development can be separated clearly.


## source layout ##

+ tpl.js: javascript template engine implementaion

+ tpl.py: python script to convert js template to bottle.py style


## basic usage ##

test.html:

	<script type="text/javascript" src="../lib/tpl.js"></script>
	<script type="text/html" id="tpl.user">
	    <% if (isboy) { %>
	        <li><%=name%> is a boy</li>
	    <% } else { %>
	        <li><%=name%> is a girl</li>
	    <% } %>
	</script>

generate bottle style template files:

	python tpl.py test .


Now you get user.tpl as below:

    %if isboy:
        <li>{{name}} is a boy</li>
    %else:
        <li>{{name}} is a girl</li>
    %end

*Please check /test directory for more examples.*
	
