INSERT INTO genero (nombre) VALUES
('Pasillo'),('Albazo'),('Sanjuanito'),('Bomba del Chota'),('Rock Ecuatoriano');

INSERT INTO artista (nombre, provincia_origen) VALUES
('Julio Jaramillo','Guayas'),
('Carlota Jaramillo','Azuay'),
('Verde 70','Pichincha'),
('AU-D','Pichincha'),
('Papá Changó','Azuay');

INSERT INTO sello (nombre) VALUES
('Independiente'),
('Sello Andino'),
('Quito Records');

INSERT INTO sucursal (nombre, ciudad) VALUES
('Sucursal Quito Centro','Quito'),
('Sucursal Guayaquil Sur','Guayaquil'),
('Sucursal Cuenca','Cuenca'),
('Sucursal Loja','Loja');

INSERT INTO disco (titulo, artista_id, genero_id, sello_id, precio, stock_total) VALUES
('Grandes Éxitos', 1, 1, 2, 9.99, 12),
('Voz del Ande', 2, 2, 2, 7.50, 8),
('Ecuador Rock', 3, 5, 1, 12.00, 5),
('Noche Quiteña', 4, 1, 3, 10.00, 7),
('Sur Andino', 5, 3, 1, 8.25, 6);

INSERT INTO movimiento (tipo, disco_id, cantidad, sucursal_destino_id, detalle) VALUES
('ENTRADA', 1, 5, 1, 'Compra inicial'),
('ENTRADA', 2, 3, 3, 'Compra inicial'),
('ENTRADA', 3, 2, 2, 'Compra inicial');