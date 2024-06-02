
INSERT INTO re_mirada_cliente
    (NOMBRE, IMAGE_URL, OCUPACION)
VALUES ('Jairo Vera', (SELECT folder || '/1.jpg' FROM re_mirada_imagefolders where id = 1),
        'Cantante urbano');


INSERT INTO re_mirada_cliente
    (NOMBRE, IMAGE_URL, OCUPACION)
VALUES ('María', (SELECT folder || '/1.jpg' FROM re_mirada_imagefolders where id = 2),
        'Novia');


INSERT INTO re_mirada_cliente
    (NOMBRE, IMAGE_URL, OCUPACION)
VALUES ('Elena', (SELECT folder || '/5.jpg' FROM re_mirada_imagefolders where id = 3),
        'Modelo');

INSERT INTO re_mirada_itemtestimonio (TESTIMONIO, CLIENTE_ID) VALUES
('¡Increíble! Las fotos del concierto capturaron la energía y la pasión de la música.', 1);

INSERT INTO re_mirada_itemtestimonio (TESTIMONIO, CLIENTE_ID) VALUES
('¡Simplemente mágico! Las fotografías de nuestra boda capturaron cada momento especial y nos permiten revivir ese día tan importante una y otra vez. Gracias por su increíble trabajo.', 2);

INSERT INTO re_mirada_itemtestimonio (TESTIMONIO, CLIENTE_ID) VALUES
('¡Me encanta! La sesión de fotos para mi retrato fue una experiencia increíble. Capturaste mi personalidad de una manera única y hermosa. ¡Gracias por tu talento y profesionalismo!', 3);


