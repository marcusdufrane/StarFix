<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <title>{{title}}</title>
  </head>
  <body>
    %for section in sections:
      <h2>{{section['name']}}</h2>
      <p>{{section['contents']}}</p>
    %end
  </body>
</html>

