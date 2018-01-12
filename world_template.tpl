<!DOCTYPE html>
<html>
<head>
	<title>Adivinar el numero</title>
</head>
<body>
	<h2>Adivina el numero</h2>

	<p>{{num}}<p>
	<p>Numero a adivinar: {{numAlt}}<p>
	<form action='/hello/world' method='post'>
		Introdueix un numero: <input type="text" name="fname">
		<input type="text" name="numAlt" value='{{numAlt}}' style='display:none'>
		<input type="submit" value="Enviar">
		<input type="submit" value="Vuelve a Empezar">
	</form>
</body>
</html>