var http = require('http');
var server = http.createServer().listen(3000);
var io = require('socket.io').listen(server);
var querystring = require('querystring');
var usuarios=0;
var denuncias=0;
var notificacio=0;

//esta en la function k escucha en evento del lado del cliente
io.on('connection', function(socket){
	//aki escuchamos el 'nuevo comentario' de los envia el cliente
	console.log("un usuario connectado");
	usuarios++;
	socket.emit('user',{numbrer:usuarios});
	socket.broadcast.emit('user',{numbrer:usuarios});

	socket.on('Aviso',informe);
	function informe(data){
		console.log(data);
		io.emit('Avisos',data);
	}
	socket.on('notificacion' ,function(data){//data son los datos que resivimos del servidor
		//console.log('escucho el evento notificacion');escucho el evento
		var values = querystring.stringify(data);
		var options = {
			hostname: 'localhost',
			port: '8000',
			path: '/crear-notificacion',
			method: 'POST',
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': values.length
			}
		};
		var request = http.request(options, function(response){
			response.setEncoding('utf8');
			response.on('data',function(data){
				//aki vienos los datos del cliente django
				io.emit('devolviendo', data);
				//console.log('emito el evento'+data)
				notificacio=notificacio+1;
				console.log('Notificacion'+notificacio);
				socket.broadcast.emit('nota',{noti:notificacio});
			});
		});
		request.write(values);
		request.end();
	});
	

socket.on('nuevo comentario' ,function(data){//data son los datos que resivimos del servidor
		var values = querystring.stringify(data);
		var options = {
			hostname: 'localhost',
			port: '8000',
			path: '/crear-comentario',
			method: 'POST', 
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': values.length
			}
		};
		var request = http.request(options, function(response){
			response.setEncoding('utf8');
			response.on('data',function(data){
				//aki vienos los datos del cliente django
				io.emit('devolviendo comentario', data);
				denuncias=denuncias+1;
				console.log('Denuncias'+denuncias)
				socket.broadcast.emit('denuncias',{denun:denuncias});
			});
		});
		request.write(values);
		request.end();
	});

	socket.on("disconnect", function(){//esta function se ejecuta cuando un usuario se desconecto del sistema
	console.log("se desconecto");
	usuarios--;
	socket.broadcast.emit('user',{numbrer:usuarios});
	});
});
