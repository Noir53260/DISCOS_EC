CREATE TABLE genero (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL UNIQUE,
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE artista (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(80) NOT NULL UNIQUE,
  provincia_origen VARCHAR(60) NOT NULL DEFAULT 'Desconocida',
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE sello (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(80) NOT NULL UNIQUE,
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE disco (
  id SERIAL PRIMARY KEY,
  titulo VARCHAR(120) NOT NULL,
  artista_id INT NOT NULL REFERENCES artista(id),
  genero_id INT NOT NULL REFERENCES genero(id),
  sello_id INT NOT NULL REFERENCES sello(id),
  precio NUMERIC(10,2) NOT NULL CHECK (precio >= 0),
  stock_total INT NOT NULL DEFAULT 0 CHECK (stock_total >= 0),
  activo BOOLEAN NOT NULL DEFAULT TRUE,
  UNIQUE (titulo, artista_id)
);

CREATE TABLE sucursal (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(70) NOT NULL UNIQUE,
  ciudad VARCHAR(60) NOT NULL,
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE movimiento (
  id SERIAL PRIMARY KEY,
  tipo VARCHAR(12) NOT NULL CHECK (tipo IN ('ENTRADA','SALIDA','TRASLADO')),
  fecha TIMESTAMP NOT NULL DEFAULT NOW(),
  disco_id INT NOT NULL REFERENCES disco(id),
  cantidad INT NOT NULL CHECK (cantidad > 0),
  sucursal_origen_id INT REFERENCES sucursal(id),
  sucursal_destino_id INT REFERENCES sucursal(id),
  detalle VARCHAR(160) NOT NULL DEFAULT '',
  CHECK (
    (tipo='ENTRADA' AND sucursal_destino_id IS NOT NULL AND sucursal_origen_id IS NULL)
    OR
    (tipo='SALIDA' AND sucursal_origen_id IS NOT NULL AND sucursal_destino_id IS NULL)
    OR
    (tipo='TRASLADO' AND sucursal_origen_id IS NOT NULL AND sucursal_destino_id IS NOT NULL AND sucursal_origen_id <> sucursal_destino_id)
  )
);