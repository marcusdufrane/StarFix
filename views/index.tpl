<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <title>StarFix</title>
  </head>
  <body>
    <h1>StarFix</h1>
    <p>Upload the STAR to be beautified!</p>
    
    <form action="/result" method="post" enctype="multipart/form-data">
      <h2>Paste it here!<h2>
      <textarea name="startext" rows="12" cols="70"></textarea>
      
      <h2>Or upload a text file here!</h2>
      <input name="starfile" type="file" />
      <br /><br />
      
      <input name="submit" type="submit" value="Beautify!" />
    </form>
  </body>
</html>

